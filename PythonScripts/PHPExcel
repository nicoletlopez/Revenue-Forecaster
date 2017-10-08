<?php
/**
 * Created by PhpStorm.
 * User: Jade_Ericson
 * Date: 8/14/2017
 * Time: 11:55 AM
 */

require_once("../PHPExcel-1.8/Classes/PHPExcel.php");

$fileName = "2015 Rooms Segmentation.xlsx";
$excelReader = PHPExcel_IOFactory::createReaderForFile($fileName);
$excelObject = $excelReader->load($fileName);
$workSheet = $excelObject->getActiveSheet();
//$lastrow = $excelObject->getHighestRow();
$excel_arr = $workSheet->toArray(null,true,true,false);

/*$multiplicand = $workSheet->getCell('F8')->getValue();
$multiplier = $workSheet->getCell('I13')->getValue();
$product = $multiplicand*$multiplier;

echo $multiplicand." * ".$multiplier." = ".$product;*/


$actualIndividual = array
(
    $rack = array(
        $jan = array(3),
        $feb = array(3),
        $mar = array(3),
        $apr = array(3),
        $may = array(3),
        $jun = array(3),
        $jul = array(3),
        $aug = array(3),
        $sep = array(3),
        $oct = array(3),
        $nov = array(3),
        $dec = array(3),
    ),
    $corp = array(
        $jan = array(3),
        $feb = array(3),
        $mar = array(3),
        $apr = array(3),
        $may = array(3),
        $jun = array(3),
        $jul = array(3),
        $aug = array(3),
        $sep = array(3),
        $oct = array(3),
        $nov = array(3),
        $dec = array(3),
    ),
    $corpOth = array(
        $jan = array(3),
        $feb = array(3),
        $mar = array(3),
        $apr = array(3),
        $may = array(3),
        $jun = array(3),
        $jul = array(3),
        $aug = array(3),
        $sep = array(3),
        $oct = array(3),
        $nov = array(3),
        $dec = array(3),
    ),
    $pack = array(
        $jan = array(3),
        $feb = array(3),
        $mar = array(3),
        $apr = array(3),
        $may = array(3),
        $jun = array(3),
        $jul = array(3),
        $aug = array(3),
        $sep = array(3),
        $oct = array(3),
        $nov = array(3),
        $dec = array(3),
    ),
    $wholeOn = array(
        $jan = array(3),
        $feb = array(3),
        $mar = array(3),
        $apr = array(3),
        $may = array(3),
        $jun = array(3),
        $jul = array(3),
        $aug = array(3),
        $sep = array(3),
        $oct = array(3),
        $nov = array(3),
        $dec = array(3),
    ),
    $wholeOff = array(
        $jan = array(3),
        $feb = array(3),
        $mar = array(3),
        $apr = array(3),
        $may = array(3),
        $jun = array(3),
        $jul = array(3),
        $aug = array(3),
        $sep = array(3),
        $oct = array(3),
        $nov = array(3),
        $dec = array(3),
    ),
    $indOth = array(
        $jan = array(3),
        $feb = array(3),
        $mar = array(3),
        $apr = array(3),
        $may = array(3),
        $jun = array(3),
        $jul = array(3),
        $aug = array(3),
        $sep = array(3),
        $oct = array(3),
        $nov = array(3),
        $dec = array(3),
    ),
    $industry = array(
        $jan = array(3),
        $feb = array(3),
        $mar = array(3),
        $apr = array(3),
        $may = array(3),
        $jun = array(3),
        $jul = array(3),
        $aug = array(3),
        $sep = array(3),
        $oct = array(3),
        $nov = array(3),
        $dec = array(3),
    ),
);
$budgetIndividual = array
(
    $rack = array(
        $jan = array(3),
        $feb = array(3),
        $mar = array(3),
        $apr = array(3),
        $may = array(3),
        $jun = array(3),
        $jul = array(3),
        $aug = array(3),
        $sep = array(3),
        $oct = array(3),
        $nov = array(3),
        $dec = array(3),
    ),
    $corp = array(
        $jan = array(3),
        $feb = array(3),
        $mar = array(3),
        $apr = array(3),
        $may = array(3),
        $jun = array(3),
        $jul = array(3),
        $aug = array(3),
        $sep = array(3),
        $oct = array(3),
        $nov = array(3),
        $dec = array(3),
    ),
    $corpOth = array(
        $jan = array(3),
        $feb = array(3),
        $mar = array(3),
        $apr = array(3),
        $may = array(3),
        $jun = array(3),
        $jul = array(3),
        $aug = array(3),
        $sep = array(3),
        $oct = array(3),
        $nov = array(3),
        $dec = array(3),
    ),
    $pack = array(
        $jan = array(3),
        $feb = array(3),
        $mar = array(3),
        $apr = array(3),
        $may = array(3),
        $jun = array(3),
        $jul = array(3),
        $aug = array(3),
        $sep = array(3),
        $oct = array(3),
        $nov = array(3),
        $dec = array(3),
    ),
    $wholeOn = array(
        $jan = array(3),
        $feb = array(3),
        $mar = array(3),
        $apr = array(3),
        $may = array(3),
        $jun = array(3),
        $jul = array(3),
        $aug = array(3),
        $sep = array(3),
        $oct = array(3),
        $nov = array(3),
        $dec = array(3),
    ),
    $wholeOff = array(
        $jan = array(3),
        $feb = array(3),
        $mar = array(3),
        $apr = array(3),
        $may = array(3),
        $jun = array(3),
        $jul = array(3),
        $aug = array(3),
        $sep = array(3),
        $oct = array(3),
        $nov = array(3),
        $dec = array(3),
    ),
    $indOth = array(
        $jan = array(3),
        $feb = array(3),
        $mar = array(3),
        $apr = array(3),
        $may = array(3),
        $jun = array(3),
        $jul = array(3),
        $aug = array(3),
        $sep = array(3),
        $oct = array(3),
        $nov = array(3),
        $dec = array(3),
    ),
    $industry = array(
        $jan = array(3),
        $feb = array(3),
        $mar = array(3),
        $apr = array(3),
        $may = array(3),
        $jun = array(3),
        $jul = array(3),
        $aug = array(3),
        $sep = array(3),
        $oct = array(3),
        $nov = array(3),
        $dec = array(3),
    ),
);

$actualGroup = array
(
    $corpMeet = array(
        $jan = array(3),
        $feb = array(3),
        $mar = array(3),
        $apr = array(3),
        $may = array(3),
        $jun = array(3),
        $jul = array(3),
        $aug = array(3),
        $sep = array(3),
        $oct = array(3),
        $nov = array(3),
        $dec = array(3),
    ),
    $conven = array(
        $jan = array(3),
        $feb = array(3),
        $mar = array(3),
        $apr = array(3),
        $may = array(3),
        $jun = array(3),
        $jul = array(3),
        $aug = array(3),
        $sep = array(3),
        $oct = array(3),
        $nov = array(3),
        $dec = array(3),
    ),
    $govt = array(
        $jan = array(3),
        $feb = array(3),
        $mar = array(3),
        $apr = array(3),
        $may = array(3),
        $jun = array(3),
        $jul = array(3),
        $aug = array(3),
        $sep = array(3),
        $oct = array(3),
        $nov = array(3),
        $dec = array(3),
    ),
    $groupTour = array(
        $jan = array(3),
        $feb = array(3),
        $mar = array(3),
        $apr = array(3),
        $may = array(3),
        $jun = array(3),
        $jul = array(3),
        $aug = array(3),
        $sep = array(3),
        $oct = array(3),
        $nov = array(3),
        $dec = array(3),
    ),
    $groupOth = array(
        $jan = array(3),
        $feb = array(3),
        $mar = array(3),
        $apr = array(3),
        $may = array(3),
        $jun = array(3),
        $jul = array(3),
        $aug = array(3),
        $sep = array(3),
        $oct = array(3),
        $nov = array(3),
        $dec = array(3),
    ),
);
$budgetGroup = array
(
    $corpMeet = array(
        $jan = array(3),
        $feb = array(3),
        $mar = array(3),
        $apr = array(3),
        $may = array(3),
        $jun = array(3),
        $jul = array(3),
        $aug = array(3),
        $sep = array(3),
        $oct = array(3),
        $nov = array(3),
        $dec = array(3),
    ),
    $conven = array(
        $jan = array(3),
        $feb = array(3),
        $mar = array(3),
        $apr = array(3),
        $may = array(3),
        $jun = array(3),
        $jul = array(3),
        $aug = array(3),
        $sep = array(3),
        $oct = array(3),
        $nov = array(3),
        $dec = array(3),
    ),
    $govt = array(
        $jan = array(3),
        $feb = array(3),
        $mar = array(3),
        $apr = array(3),
        $may = array(3),
        $jun = array(3),
        $jul = array(3),
        $aug = array(3),
        $sep = array(3),
        $oct = array(3),
        $nov = array(3),
        $dec = array(3),
    ),
    $groupTour = array(
        $jan = array(3),
        $feb = array(3),
        $mar = array(3),
        $apr = array(3),
        $may = array(3),
        $jun = array(3),
        $jul = array(3),
        $aug = array(3),
        $sep = array(3),
        $oct = array(3),
        $nov = array(3),
        $dec = array(3),
    ),
    $groupOth = array(
        $jan = array(3),
        $feb = array(3),
        $mar = array(3),
        $apr = array(3),
        $may = array(3),
        $jun = array(3),
        $jul = array(3),
        $aug = array(3),
        $sep = array(3),
        $oct = array(3),
        $nov = array(3),
        $dec = array(3),
    ),
);

//echo $excel_arr[7][3];
$actualRow=7;
$budgetRow=8;
$indcol=3;
$grpcol=30;
for($ss=0;$ss<count($actualIndividual);$ss++){
    for($m=0;$m<count($actualIndividual[0]);$m++){
		//echo "[".$row."]"."[".$col."] month#: ".$m." subsegment#: ".$ss."<br/>";
        $actualIndividual[$ss][$m][0] = $excel_arr[$actualRow][$indcol];
        $actualIndividual[$ss][$m][1] = $excel_arr[$actualRow][$indcol+1];
        $actualIndividual[$ss][$m][2] = $excel_arr[$actualRow][$indcol+2];
        $actualRow+=4;
    }
    $actualRow=7;
    $indcol+=3;
	//echo $col."<br/>";
}

for($ss=0;$ss<count($actualGroup);$ss++){
    for($m=0;$m<count($actualGroup[0]);$m++){
        //echo "[".$row."]"."[".$col."] month#: ".$m." subsegment#: ".$ss."<br/>";
        $actualGroup[$ss][$m][0] = $excel_arr[$actualRow][$grpcol];
        $actualGroup[$ss][$m][1] = $excel_arr[$actualRow][$grpcol+1];
        $actualGroup[$ss][$m][2] = $excel_arr[$actualRow][$grpcol+2];
        $actualRow+=4;
    }
    $actualRow=7;
    $grpcol+=3;
    //echo $col."<br/>";
}

for($ss=0;$ss<count($budgetIndividual);$ss++){
    for($m=0;$m<count($budgetIndividual[0]);$m++){
        //echo "[".$row."]"."[".$col."] month#: ".$m." subsegment#: ".$ss."<br/>";
        $budgetIndividual[$ss][$m][0] = $excel_arr[$budgetRow][$indcol];
        $budgetIndividual[$ss][$m][1] = $excel_arr[$budgetRow][$indcol+1];
        $budgetIndividual[$ss][$m][2] = $excel_arr[$budgetRow][$indcol+2];
        $budgetRow+=4;
    }
    $budgetRow=7;
    $indcol+=3;
    //echo $col."<br/>";
}

for($ss=0;$ss<count($budgetGroup);$ss++){
    for($m=0;$m<count($budgetGroup[0]);$m++){
        //echo "[".$row."]"."[".$col."] month#: ".$m." subsegment#: ".$ss."<br/>";
        $budgetGroup[$ss][$m][0] = $excel_arr[$budgetRow][$grpcol];
        $budgetGroup[$ss][$m][1] = $excel_arr[$budgetRow][$grpcol+1];
        $budgetGroup[$ss][$m][2] = $excel_arr[$budgetRow][$grpcol+2];
        $budgetRow+=4;
    }
    $budgetRow=7;
    $grpcol+=3;
    //echo $col."<br/>";
}


echo '<pre>'; print_r($actualIndividual); echo '</pre>';
/*
echo '<pre>'; print_r($actualGroup); echo '</pre>';
echo '<pre>'; print_r($budgetIndividual); echo '</pre>';
echo '<pre>'; print_r($budgetGroup); echo '</pre>';*/
?>