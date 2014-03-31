<!DOCTYPE html>
<html>

<head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Start Bootstrap - SB Admin Version 2.0 Demo</title>

    <!-- Core CSS - Include with every page -->
    <link href="/staticfiles/css/bootstrap.min.css" rel="stylesheet">
    <link href="/staticfiles/font-awesome/css/font-awesome.css" rel="stylesheet">
	<link href="/staticfiles/css/zebra_datepicker.css" rel="stylesheet">

    <!-- Page-Level Plugin CSS - Blank -->

    <!-- SB Admin CSS - Include with every page -->
    <link href="/staticfiles/css/sb-admin.css" rel="stylesheet">

</head>

<body>

    <div id="wrapper">

        <nav class="navbar navbar-default navbar-static-top" role="navigation" style="margin-bottom: 0">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".sidebar-collapse">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="/admin">ADMIN name here</a>
            </div>
            <!-- /.navbar-header -->
        </nav>
        <!-- /.navbar-static-top -->

        <nav class="navbar-default navbar-static-side" role="navigation">
            <div class="sidebar-collapse">
                <ul class="nav" id="side-menu">
                    <li class="sidebar-search">
                        <div class="input-group custom-search-form">
                            <a href="/adminlogout">Logout</a>
                        </div>
                        <!-- /input-group -->
                    </li>
                    <li>
                        <a href="index.html"><i class="fa fa-dashboard fa-fw"></i> Dashboard</a>
                    </li>
                </ul>
                <!-- /#side-menu -->
            </div>
            <!-- /.sidebar-collapse -->
        </nav>
        <!-- /.navbar-static-side -->

        <div id="page-wrapper">
            <div class="row">
                <div class="col-lg-12">
                    <br>
                    <br>
                    <br>
                    <br>
                    <br>
                    <div class="col-xs-4">
                        <div class="panel panel-primary">
                            <div class="panel-heading">Status</div>
                            <div class="panel-body">
                                <br>
                                <br>
                                <div class="table-responsive">
                                    <table class="table">
                                        <tbody>
                                          <tr class="success">
                                              <td>Humans</td>
                                              <td class="humans">0</td>
                                          </tr>
                                          <tr class="warning">
                                              <td>Temperature</td>
                                              <td class="temperature">0</td>
                                          </tr>
                                            <tr class="info">
                                              <td>Light</td>
                                              <td class="light">0</td>
                                          </tr>
                                        </tbody>

                                    </table>
                                </div>

                            </div>
                        </div>
                    </div>
                    <div class="col-xs-4">
                        <div class="panel panel-primary">
                            <div class="panel-heading">create event</div>
                            <div class="panel-body">
                                <form role="form" action="/createevent" method="post">
                                    <div class="form-group">
                                        <label class="control-label">Event name</label>
                                        <input type="text" name="eventname" class="form-control" placeholder="enter event name">
                                    </div>
                                    <div class="form-group">
                                        <label class="control-label">Event Date</label>
                                        <input type="text" name="eventdate" class="form-control" placeholder="click for event date" id="eventdate">
                                    </div>
                                    <div class="form-group">
                                        <label class="control-label">Maximum humans </label>
                                        <input type="text" name="maxhumans" class="form-control" placeholder="enter number of people expected">
                                    </div>
                                    <button type="submit" class="btn btn-primary">submit</button>
                                </form>
                            </div>
                        </div>
                    </div>
                    <div class="col-xs-4">
                        <div class="panel panel-primary">
                            <div class="panel-heading">set conditions</div>
                            <div class="panel-body"></div>
                        </div>
                    </div>
                </div>
                <!-- /.col-lg-12 -->
            </div>
            <!-- /.row -->
        </div>
        <!-- /#page-wrapper -->

    </div>
    <!-- /#wrapper -->

    <!-- Core Scripts - Include with every page -->
    <script src="/staticfiles/js/jquery-1.10.2.js"></script>
    <script src="/staticfiles/js/bootstrap.min.js"></script>
    <script src="/staticfiles/js/plugins/metisMenu/jquery.metisMenu.js"></script>

    <!-- Page-Level Plugin Scripts - Blank -->

    <!-- SB Admin Scripts - Include with every page -->
    <script src="/staticfiles/js/sb-admin.js"></script>
    <script src="/staticfiles/js/zebra_datepicker.js"></script>
    <script type="text/javascript">
	    $(document).ready(function(){
		    $('#eventdate').Zebra_DatePicker();
		    setInterval(function(){
		    var url = '/getdata'
    		$.ajax({
                url:url,
                type:"GET",
                async:false,
                success:function(data){
                    $('.humans').text(data);
                    $('.temperature').text(data);
                    $('.light').text(data);
                }
		    });

		    },5000);
	    });

	</script>


</body>

</html>
