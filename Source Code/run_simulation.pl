# This will be run through power directory

unless($ARGV[0])
{
  die "*ERROR: Give project name \n".
  "Usage:  RunSim.sh <Project_name> <power_type> <module_name> <model_file_path>\n";
}
unless($ARGV[1])
{
  # ActivePwr or StandbyPwr
  die "*ERROR: Give type of power calculation: ActivePwr | StandbyPwr\n".
  "Usage:  RunSim.sh <param_file> <power_type> <module_name> <model_file_path>\n";
}
unless($ARGV[2])
{
  die "*ERROR: Give module name \n".
  "Usage:  RunSim.sh <Project_name> <power_type> <module_name> <model_file_path>\n";
}

unless($ARGV[3])
{
  die "*ERROR: Give model file path \n".
  "Usage:  RunSim.sh <Project_name> <power_type> <module_name> <model_file_path>\n";
}
## Get sim_parameters

my $moduleName = $ARGV[2];
my $sourceLocLib = $ARGV[3];
my $SupplyVal, $totTime, $stepSize;
my $hashLoadCaps = {};
my $hashPulse = {};
my $hashDCinp = {};

# Read the sim_parameters file to get the user specified simulation parameters
open(FILE, '<', "../sim_parameters/$ARGV[0]"."_".$ARGV[1]."_param.txt")
  or die "Could not find parameter file- $!";
while (my $row = <FILE>) {
  if(index(lc($row),"supply") == 0)
  {
    my @array = split(" ", $row);
    $SupplyVal = $array[1];
  }
    if(index(lc($row),"stop time") == 0)
  {
    my @array = split(" ", $row);
    $totTime = $array[2];
  }
    if(index(lc($row),"step size") == 0)
  {
    my @array = split(" ", $row);
    $stepSize = $array[2];
  }
    if(index(lc($row),"input pulse") == 0)
  {
    my @array = split(" ", $row);
    $hashPulse->{$array[2]} = {};
    $hashPulse->{$array[2]}{'initial'} = $array[4];
    $hashPulse->{$array[2]}{'pulsed'} = $array[6];
    $hashPulse->{$array[2]}{'delay'} = $array[8];
    $hashPulse->{$array[2]}{'rise_time'} = $array[10];
    $hashPulse->{$array[2]}{'fall_time'} = $array[12];
    $hashPulse->{$array[2]}{'pulse_width'} = $array[14];
    $hashPulse->{$array[2]}{'period'} = $array[16];
  }
    if(index(lc($row),"input dc") == 0)
  {
    my @array = split(" ", $row);
    $hashDCinp->{$array[2]} = $array[3];
  }
    if(index(lc($row),"load") == 0)
  {
    my @array = split(" ", $row);
    $hashLoadCaps->{$array[1]} = $array[2];
  }
}
close(FILE);

## MAIN ##

my $filename = "./$ARGV[0]"."_@ARGV[1]".".spice"; # Final spice netlist
open(my $fh, '>', $filename) or die "Could not open file $filename-$!";

# Add library
print $fh ".LIB ".'"'.$sourceLocLib.'"'." cmos_models\n";   
close $fh;

# Add subcomponents spice definitions 
system("cat ../spice_netlist/*.spice >> $filename");

open(COMMANDS, '>>', "$filename") 
  or die "Could not open file $ARGV[1]-$!";
select(COMMANDS);

add_supply($SupplyVal);                       
add_subckt_call($moduleName);
add_load_caps($hashLoadCaps);
add_input_pulse($hashPulse);
add_input_dc($hashDCinp);                        
add_tran($totTime, $stepSize);
add_power_equations($totTime);

select(STDOUT);
close(COMMANDS);

system("sed -i 's/nfet/nmos/g' $filename");  # Converting nfet to nmos to match library
system("sed -i 's/pfet/pmos/g' $filename");  # Converting pfet to pmos to match library

#Running ngspice
system("ngspice $filename<<EOF
run
exit
EOF");

### SUBS ###

# To add user specified Supply value 
sub add_supply
{
  my $loSupply = shift;
  my $string = ".param gnd = 0
.param SUPPLY = $loSupply
.GLOBAL vdd gnd
Vdd vdd gnd $loSupply".'V';
  print $string."\n";
}

# To call main sub circuit
sub add_subckt_call
{
  my $loModuleName = shift;
  my $loParentSpiceFile = "../spice_netlist/$loModuleName".".spice";
  open(FILE, '<', $loParentSpiceFile)
    or die "Could not open file $loParentSpiceFile- $!";
  my @rows = <FILE>;
  my $num = @rows;
  for(my $i = 0; $i < $num; $i++) {
      my $row = $rows[$i];
      if(index($row,".subckt $loModuleName") == 0)
      {
        my @array = split(" ", $row);
        shift(@array);
        shift(@array);
        my $string = join(" ", @array);
        print "Xmain $string ";
        $i = $i + 1;
        $row = $rows[$i];
        while(index($row,"+ ") == 0) {
          @array = split(" ", $row);
          shift(@array);
          $string = join(" ", @array);
          print "$string ";
          $i = $i + 1;
          $row = $rows[$i];
        }
        print "$loModuleName\n";
        last;
      }
  }
}

# To add load capacitances
sub add_load_caps
{
  my $loHashLoadCaps = shift;
  my $caps = "";
  foreach $node (keys %{$loHashLoadCaps})
  {
    $caps = $caps."\ncap_"."$node $node gnd ".$loHashLoadCaps->{"$node"};
  }
  print $caps."\n";
}

# To add user specified input pulse
sub add_input_pulse
{
  my $loPulseHash = shift;
  my $string = "";
  foreach $node (keys %{$loPulseHash})
  {
    $string = $string."\nVin_$node $node 0 0 pulse ".$loPulseHash->{$node}{'initial'}." ".
    $loPulseHash->{$node}{'pulsed'}." ".$loPulseHash->{$node}{'delay'}." ".
    $loPulseHash->{$node}{'rise_time'}." ".$loPulseHash->{$node}{'fall_time'}." ".
    $loPulseHash->{$node}{'pulse_width'}." ".$loPulseHash->{$node}{'period'};
  }
  print "$string\n";
}

# To add user specified dc inputs
sub add_input_dc
{
  my $loDCinpHash = shift;
  my $string = "";
  foreach $node (keys %{$loDCinpHash})
  {
    $string = $string."\nVin_$node $node gnd ".$loDCinpHash->{$node};
  }
  print "$string\n";
}

sub add_tran
{
  my $loTotTime = shift;
  my $loStepSize = shift;
  my $string = ".tran $loStepSize $loTotTime";
  print "$string\n";
}

# To add commands for power calculation
sub add_power_equations
{
  my $loTotTime=shift;
  my $string = ".measure tran total_q integ i(vdd) from = 0 to = $loTotTime
.measure tran energy_avg param = '-SUPPLY*total_q'
.measure tran power_avg_absolute param = '-(SUPPLY*total_q)/$loTotTime' ***absolute power
.measure tran power_avg_uW param = '-(SUPPLY*total_q)/($loTotTime*1u)' ***power in uW

.end
";
  print "$string\n";
}
