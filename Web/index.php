<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Jua&display=swap" rel="stylesheet">

<?php
$conn = mysqli_connect(
  'localhost',
  'root',
  'qwerty1234',
  'bookreview');

// 책 대비 리포트 수
$per = array(
  'book_num',
  'report_num'
);
  
$sql1 = "select count(*) from bookreport";
$sql2 = "select count(*) from book";

$result1 = mysqli_query($conn, $sql1);
$row1 = mysqli_fetch_array($result1);
$per['report_num'] = htmlspecialchars($row1['count(*)']);

$result2 = mysqli_query($conn, $sql2);
$row2 = mysqli_fetch_array($result2);
$per['book_num'] = htmlspecialchars($row2['count(*)']);

$report_per_book="<h2 style='background-color:white;'>리뷰 수/책 수</h2>"."<h4>{$per['report_num']}/{$per['book_num']}</h4></br></br></br></br></br>";



// 이달의 리뷰 왕
$reviewking = array(
  'name', 'count'
);
  
$sql3 = "SELECT name, count(*) from bookreport left join user on user.id=bookreport.uid group by 1 order by 2 desc limit 3";
$result3 = mysqli_query($conn, $sql3);

$review_wang="<h2 style='background-color:white;'> 리뷰 왕</h2>";
while($row = mysqli_fetch_array($result3)) {
    $reviewking['name'] = htmlspecialchars($row['name']);
    $reviewking['count'] = htmlspecialchars($row['count(*)']);

    $review_wang = $review_wang."<h4>{$reviewking['name']} : {$reviewking['count']}개</h4>";
  
}


// 베스트 셀러
$bestseller = array(
  'title', 'count'
);
  
$sql4 = "SELECT title, count(*) from bookreport left join book on book.bnum=bookreport.bnum group by 1 order by 2 desc limit 3";
$result4 = mysqli_query($conn, $sql4);

$bestseller_list="<h2 style='background-color:white;'>베스트 셀러</h2>";
while($row = mysqli_fetch_array($result4)) {
    $bestseller['title'] = htmlspecialchars($row['title']);
    $bestseller['count'] = htmlspecialchars($row['count(*)']);

    $bestseller_list = $bestseller_list."<h4>{$bestseller['title']} : {$bestseller['count']}개</h4>";
  
}


// 리포트 리스트
$sql = "SELECT * from bookreport p left join book b on p.Bnum=b.Bnum order by p.bnum";
$result = mysqli_query($conn, $sql);
$list = '';
while($row = mysqli_fetch_array($result)) {
  $escaped_title = htmlspecialchars($row['title']);
  $list = $list."<li><a href=\"index.php?Pid={$row['Pid']}\">{$escaped_title}</a></li>";
}


// 리뷰
$article = array(
  'title'=>'Welcome',
  'Remarks'=>"책 제목에 대한 리뷰",
  'Author'=>"작가"
);

$update_link = '';
$delete_link = '';
$author = '';
if(isset($_GET['Pid'])) {
  $filtered_id = mysqli_real_escape_string($conn, $_GET['Pid']);
  $sql = "select * from bookreport p left join book b on p.Bnum=b.Bnum where p.Pid={$filtered_id}";

  $result = mysqli_query($conn, $sql);
  $row = mysqli_fetch_array($result);
  $article['title'] = htmlspecialchars($row['title']);
  $article['Remarks'] = htmlspecialchars($row['Remarks']);
  $article['Author'] = htmlspecialchars($row['Author']);

  //$update_link = '<a href="update.php?Pid='.$_GET['Pid'].'">update</a>';
  $update_link = '
    <form action="update.php?Pid='.$_GET['Pid'].'" method="post">
      <input type="hidden" name="Pid" value="'.$_GET['Pid'].'">
      <input type="submit" value="update" class="btn">
    </form>
  ';
  $delete_link = '
    <form action="process_delete.php" method="post">
      <input type="hidden" name="Pid" value="'.$_GET['Pid'].'">
      <input type="submit" value="delete" class="btn">
    </form>
  ';
  $author = "<p>by {$article['Author']}</p>";
}
?>

<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>도서 리뷰 관리 시스템</title>
    <link rel="stylesheet" href="main.css">
  </head>
  <body>
    <div id='jb-container'>
      <div id='jb-header'><h1><a href="index.php">도서 관리 시스템</a></h1></div>
      <div id='jb-sidebar-left'><?=$report_per_book?></div>
      <div id='jb-content'><?=$bestseller_list?></div>
      <div id='jb-sidebar-right'><?=$review_wang?></div>
      <div id="jb-footer"><h2><a href="Book.php">Book Information</a></h2></div>
      </br>
      <div id="jb-footer"><h2>Review List</h2></div>
      </br>
      <div id="jb-footer" style="overflow:auto; height:300px;">
        <ol class="mylist">
          <?=$list?>
        </ol>
      </div>
      </br>
      <div id="jb-footer">
        <form action="create.php" method="post">
          <input type="hidden" name="Pid" value="'.$_GET['Pid'].'">
          <input type="submit" value="create" class="btn">
        </form><?=$update_link?><?=$delete_link?>
      </div>
      </br>
      <div id="jb-footer">
        <h2><?=$article['title']?></h2>
        <?=$article['Remarks']?>
        <?=$author?>
      </div>
    </div>
  </body>
</html>
