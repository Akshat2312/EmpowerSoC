my $ScriptLoc = "/usr/lib/EmpowerSoc";
my $moduleName;


opendir(DIR, '../synthesis') or die "Couldn't open directory, $!";
my @blifFile = grep(/\.blif$/,readdir(DIR));
#print $blifFile[0]."\n";
close(DIR);

# Reading the .blif file to get the module name
open(FILE, '<', "../synthesis/$blifFile[0]")
  or die "Could not open file $blifFile[0]- $!";

while (my $row = <FILE>) {
  if(index($row,".model") == 0)
  {
  	my @array = split(" ", $row);
  	#print "Module name - $array[1]\n";
  	$moduleName=$array[1];
  	last;
  }
}
close(FILE);

# Calling create_magic_load_file.sh script to create load_<moduleName>.tcl file
system("$ScriptLoc/create_magic_load_file.sh .. $moduleName"); 

# Running Magic tool to create .ext files for subcomponents 
my $command = "magic -dnull -noconsole ".$moduleName.".mag<<EOF
source load_".$moduleName.".tcl
extract all
quit -noprompt
EOF";
system($command);

# Using Magic tool to extract .spice files of subcomponents
opendir(DIR, '.') or die "Couldn't open directory, $!";
my $files="";
foreach (sort grep(/\.ext$/,readdir(DIR))) {
    $files=$files."ext2spice $_\n";
   }
$files=$files."quit -noprompt\n";
$files =~ s/\.ext//g;
#print $files;
$command = "magic -noconsole -nowrapper ".$moduleName.".mag<<EOF
$files
EOF";
system($command);

# Storing the spice netlists inside EmpowerSOC/spice_netlist directory
if( -d "../EmpowerSOC/spice_netlist")
{
  system("rm -rf ../EmpowerSOC/spice_netlist");
}
system("mkdir ../EmpowerSOC/spice_netlist");
system("mv *.spice ../EmpowerSOC/spice_netlist");
