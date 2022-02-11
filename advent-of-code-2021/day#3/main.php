<?php


class DayThree {

    public array $gameboard;
    public array $structure;
    public int $row;
    public int $col;

    public function __construct(){
        $this->gameboard = [[]];
        $this->row = 0;
        $this->col = 0;
        $this->structure = [];


    }

    public function PartOne(){
        $handle = fopen("input.txt", "r");
        if ($handle) while (($line = fgets($handle)) !== false) {
            $temp = trim($line);
            $x = str_split($temp);
            array_push($this->structure, $x);
            
            for($i = 0; $i < count($this->gameboard); $i++){
                $mid = count($this->gameboard) / 2;
                $count = 0;
                for($j = 0; $j < count($this->gameboard); $j++){
                    if ($this->gameboard[$i][$j] == "1") $count += 1;
                    if ($this->gameboard[$i][$j] == "0") $count -= 1;
                }
                if ($count > $mid) {
                    echo "1";
                } else if ($count < $mid){
                    echo "0";
                } else {
                    echo "00";
                }
            }
            echo "\n";

        }
    
        print_r($this->gameboard);
        unset($handle);
    }
}

$x = new DayThree();
$x->PartOne();




/*
$gameboard = [[0, 0, 0], [0, 0, 0],[0, 0, 0]];
$rowLength = count($gameboard);
$column = count($gameboard[0]);

$menu = true;


$i = 0;
while ($i < $rowLength){
    $row = $i;
    $col = 0;
    $arr += $gameboard[$row][$col];

    $i++;
}

for ($i = 0; $i < $rowLength; $i++){
    $row = $i;
}

function check_win($lists){
    if(count($lists[0])
}


*/