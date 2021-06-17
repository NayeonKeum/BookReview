<?php
$conn = mysqli_connect(
  'localhost',
  'root',
  'qwerty1234',
  'bookreview');

$filtered = array(
  'Uid'=>mysqli_real_escape_string($conn, $_POST['ID']),
  'Bnum'=>mysqli_real_escape_string($conn, $_POST['Bnum']),
  'Remarks'=>mysqli_real_escape_string($conn, $_POST['Remarks'])
);

// 저장 
$sql = "
  INSERT INTO bookreport
    (Uid, Bnum, date, rating, Remarks)
    VALUES(
        '{$filtered['Uid']}',
        '{$filtered['Bnum']}',
        NOW(),
        0,
        '{$filtered['Remarks']}'
    )
";

$result = mysqli_query($conn, $sql);
if($result === false){

  echo '저장하는 과정에서 문제가 생겼습니다. 관리자에게 문의해주세요';
} else {
  echo '성공했습니다. <a href="index.php">돌아가기</a>';
}

?>
