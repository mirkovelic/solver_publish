#!/usr/bin/perl
$sump=0;
$sumv=0;
$timep=0;
$nlits=0;
  
while(<STDIN>){
    if(/^\|\s*(?P<pits>\d+)\s*\|\s*(\d+)\s*\|(\s*\d+\.\d+\s*)\|(?P<cons>\s*[.-\w]+\s*)\|((?P<pen>\s*[ .-\w]+\s*)\|){8}(?P<pc>\s*[ .-\w]+\s*)\|\s*(?P<scaled>\d+)\s*\|((?P<res>\s*[ .-\w]+\s*)\|){6}/){  #using named groups
        print "$1 $+{pits} $2 $5 $+{pen} $+{cons} $+{pc} scaled=$+{scaled} res=$+{res}\n";
    }
}

