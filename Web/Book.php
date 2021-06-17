<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Jua&display=swap" rel="stylesheet">

<?php
$conn = mysqli_connect(
  'localhost',
  'root',
  'qwerty1234',
  'bookreview');
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
      <div id="jb-footer">
        <table border="1">
        <thead>
          <tr>
            <th scope="cols">Bnum</th>
            <th scope="cols">Author</th>
            <th scope="cols">title</th>
            <th scope="cols">Publisher</th>
          </tr>
        </thead>
        <tbody>
        <tr>
          <?php
          $sql = "SELECT * FROM book";
          $result = mysqli_query($conn, $sql);
          while($row = mysqli_fetch_array($result)){
            $filtered = array(
              'Bnum'=>htmlspecialchars($row['Bnum']),
              'Author'=>htmlspecialchars($row['Author']),
              'title'=>htmlspecialchars($row['title']),
              'Publisher'=>htmlspecialchars($row['Publisher']),
            );
            ?>
            <tr>
              <td><?=$filtered['Bnum']?></td>
              <td><?=$filtered['Author']?></td>
              <td><?=$filtered['title']?></td>
              <td><?=$filtered['Publisher']?></td>
            </tr>
            <?php
          }
          ?>
        </tr>
        </tbody>
      </table>
      </div>
    </div>
  </body>
</html>
