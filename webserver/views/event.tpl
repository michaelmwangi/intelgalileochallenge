<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Events</title>

    <!-- Bootstrap core CSS -->
    <link href="/staticfiles/css/bootstrap.css" rel="stylesheet">

    <!-- Custom CSS for the 'Heroic Features' Template -->
    <link href="/staticfiles/css/heroic-features.css" rel="stylesheet">
    <style>
    #box{
      margin-top:10px;
    }
    </style>
  </head>

  <body>
    <div class="container">
	<div class="row">
	    <div class="col-lg-6 col-lg-offset-3" id="box">
             <div class="panel panel-primary">
                <div class="panel-heading">Events</div>
                <div class="panel-body">
                    <div class="table-responsive">
                        <table class="table">
                            <thead>
                                <tr>
                                    <td>event date</td>
                                    <td>event name</td>
                                </tr>
                            </thead>
                            <tbody>
                                    %if events:
                                        %for event in events:
                                            <tr>
                                            <td>{{event[0]}}</td>
                                            <td>{{event[1]}}</td>
                                             </tr>
                                        %end
                                    %else:
                                          <td>There are currently no events</td>
                                    %end


                            </tbody>
                        </table>
                    </div>
                    %if events:
                        <form role="form" action="/eventsignup" method="post">
                             <fieldset>
                                <div class="form-group">
                                    <label>Email :</label>
                                    <input class="form-control" placeholder="E-mail" name="email" type="email" autofocus>
                                </div>
                                <div class="form-group">
                                    <label>Choose event:</label>
                                    <select name="eventname">
                                        %for event in events:
                                                <option >{{event[1]}}</option>
                                         %end
                                    </select>
                                </div>
                                <!-- Change this to a button or input when using this as a form -->
                                <button type="submit" class="btn btn-lg btn-success btn-block">Attend</button>
                            </fieldset>
                        </form>
                    %end
                </div>
             </div>
	    </div>
	</div>
         <hr>

      <footer>
        <div class="row">
          <div class="col-lg-12">
            <p>Copyright &copy; #</p>
          </div>
        </div>
      </footer>
      
    </div><!-- /.container -->

    <!-- JavaScript -->

    <!-- Core Scripts - Include with every page -->
    <script src="/staticfiles/js/jquery-1.10.2.js"></script>
    <script src="/staticfiles/js/bootstrap.min.js"></script>
    <script src="/staticfiles/js/plugins/metisMenu/jquery.metisMenu.js"></script>

    <!-- SB Admin Scripts - Include with every page -->
    <script src="/staticfiles/js/sb-admin.js"></script>


  </body>

</html>