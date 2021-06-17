<?php
$conn = mysqli_connect(
  'localhost',
  'root',
  'qwerty1234',
  'bookreview');

$filtered = array(
  'Pid'=>mysqli_real_escape_string($conn, $_POST['Pid'])
);

$sql = "
  DELETE
    FROM bookreport
    WHERE Pid = {$filtered['Pid']}
";
$result = mysqli_query($conn, $sql);
if($result === false){
  echo '저장하는 과정에서 문제가 생겼습니다. 관리자에게 문의해주세요';
  error_log(mysqli_error($conn));
} else {
  echo '삭제에 성공했습니다. <a href="index.php">돌아가기</a>';
}
?>
