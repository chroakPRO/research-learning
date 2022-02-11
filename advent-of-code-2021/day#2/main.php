<?php

class DayTwo {

    public int $up;
    public int $down;
    public int $forward;
    public int $horizontal;
    public int $depth;
    public int $total;
    public int $aim;

    public function __construct(){
        $this->forward = 0;
        $this->down = 0;
        $this->up = 0;
        $this->horizontal = 0;
        $this->depth = 0;
        $this->total = 0;
        $this->aim = 0;
    }

    public function PartOne()
    {
        $handle = fopen("input.txt", "r");
        if ($handle) {
            while (($line = fgets($handle)) !== false) {
                $x = explode(" ", $line);
                if ($x[0] == "forward") $this->horizontal += $x[1];
                else if ($x[0] == "up") $this->depth -= $x[1];
                else if ($x[0] == "down") $this->depth += $x[1];
                else echo "error";
            }
        }
        unset($handle);
        $this->total = ($this->horizontal * $this->depth);
    }

    public function PartTwo()
    {
        $handle = fopen("input.txt", "r");
        if ($handle) {
            while (($line = fgets($handle)) !== false) {
                $x = explode(" ", $line);
                if ($x[0] == "forward") {
                    $this->horizontal += $x[1];
                    if ($this->aim != 0){
                        $this->depth += ($this->aim * $x[1]);
                        echo "Aim";
                        echo $this->aim;
                        echo "\n";
                    }
                } else if ($x[0] == "up"){
                    $this->aim -= $x[1];
                    echo "Aim";
                    echo $this->aim;
                    echo "\n";
                } else if ($x[0] == "down") {
                    $this->aim += $x[1];
                    echo "Aim";
                    echo $this->aim;
                    echo "\n";
                }
            }
        }
        $this->total = ($this->horizontal * $this->depth);
    }

}

$x = new DayTwo();
$x->PartOne();
echo "Part One -> ";
echo $x->total;
echo "\n";
$x2 = new DayTwo();
$x2->aim = 0;
$x2->PartTwo();
echo "Part Two -> ";
echo $x2->total;

echo "\n";