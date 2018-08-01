
var stuObj = {};
$(function () {
    //初始化拍照控件
    webcam.set_api_url('../ashx/Handler1.ashx?Method=SavePic');
    webcam.set_quality(90); // JPEG quality (1 - 100)
    webcam.set_shutter_sound(true, "../Scripts/jepgcam/shutter.mp3"); // play shutter click sound
    webcam.set_swf_url("../Scripts/jepgcam/webcam.swf");
    webcam.set_hook('onComplete', 'my_completion_handler');
    webcam.set_hook('onError', 'myerror');
    $("#myCam").html(webcam.get_html(320, 240));

    //学员当前学车类型
    var sub = $("#sub").val();
    stuObj.mykm = 1;//初始化科目一
    stuObj.km1 = $("#km1").val();//科目一学时
    stuObj.km4 = $("#km4").val();//科目四学时
    stuObj.sub = sub;
    //如果科目一学时已满直接学习科目四
    if (stuObj.km1 >= xsobj[sub + '1'] * 60) {
        stuObj.mykm = 4;
        $("#dqkm").html("科目四");
    }
    stuObj.btime = stuObj["km" + stuObj.mykm] * 60;
    stuObj.bctime = 0;//本次时间
    stuObj.lastF = parseInt(stuObj.btime / (5 * 60));
    stuObj.sec = 0;//秒数
    stuObj.beginStu = false;
    stuObj.hasCam = true;
    stuObj.sbtime = 0;
    $("#yx").html(toHourMinute(stuObj.btime));       
    setKm(stuObj.mykm);    
});
//其他頁面开始学习
function setBegin(cp) {
    if (isjh!=1) {
        alert("请先支付！");
        return;
    }
    if (stuObj.beginStu) {
        return;
    }
    stuObj.cpid = cp;
    stuObj.beginStu = true;
    start();
    //console.log("46");
}
//设置相机上传科目
function setKm(km) {
    webcam.set_api_url('../ashx/Handler1.ashx?Method=SavePic&km='+km);
}
//结束学习
function setEnd() {
    stuObj.beginStu = false;
    //console.log("setend");
    stop();
}
//其他頁面獲取學習狀態
function getBeginStu() {
    return stuObj.beginStu;
}
//攝像頭調用失敗
function myerror(msg) {
    if (msg = "No camera was detected.") {
        alert("请连接摄像头！否则无法学习！");
        stuObj.hasCam = false;
    }
}
//跳转其他页面
function changeFrame(url) {
    
    if (isjh != 1) {
        alert("请先支付！");
        return;
    }
     
    if (stuObj.beginStu) {
        jQuery.messager.confirm('提示:', '你确认要退出学习吗?', function (event) {
            if (event) {
                setEnd();
                $("#mainFrame").attr("src", url);
            } else {
                return;
            }
        });

    } else {
        if (url.indexOf("zhangjie") == 0 && !stuObj.hasCam) {
            alert("请连接摄像头！否则无法学习！");
            return; 
        }
        $("#mainFrame").attr("src", url);
    }
}
//调用拍照接口
function pz() {        
    webcam.snap();
}
//格式化日期
function toHourMinute(time) {
    if (null != time && "" != time) {
        if (time > 60 && time < 60 * 60) {
            time = parseInt(time / 60.0) + "分" + parseInt((parseFloat(time / 60.0) -
		                parseInt(time / 60.0)) * 60) + "秒";
        }
        else if (time >= 60 * 60 && time < 60 * 60 * 24) {
//            var ss = parseInt((parseFloat((parseFloat(time / 3600.0) - parseInt(time / 3600.0)) * 60) -
//		                    parseInt((parseFloat(time / 3600.0) - parseInt(time / 3600.0)) * 60)) * 60);
            var ss = time % 60;
            var fen = (time - ss) % (60 * 60)/60;
            time = parseInt(time / 3600.0) + "时" + (fen > 0 ? (fen + "分") : "") + (ss > 0 ? (ss + "秒") : "");
		                    
        }
        else {
            time = parseInt(time) + "秒";
        }
    }
    return time;
}
//拍照完成后回调
function my_completion_handler(msg) {
    eval("var data=" + msg);
    //console.log("my_completion_handler");
    if (data.isOk == 0) {
        if (data.message.indexOf("今日学时已满") >= 0) {
            alert(data.message);
            window.location.href = "Main.aspx";
        } else if (data.message.indexOf("人脸识别失败") >= 0){
            alert(data.message);
            stuObj.sec = stuObj.sec - 5;
            stuObj.sbtime = stuObj.sbtime+1;
            if (stuObj.sbtime > 5) {
                window.location.href = "Main.aspx";
                stuObj.sbtime = 0;
                return;
            }
           
        } else {
            stuObj.hasCam = false;
            alert("请连接摄像头并点击“允许”进入学习！");
            window.location.href = "Main.aspx";
        }
        stuObj.lastF = stuObj.lastF - 1;
        restart();
        //console.log("144");
    } else {
        stuObj.sbtime = 0;
        checkCode();
        stuObj.hasCam = true;
    }
    webcam.reset();
    ////console.log((new Date()) + ":saveimg");
}
function setJh(val) {
    
    isjh = val;
}
var isjh = 0;
var xsobj = { 'A11': 10, 'A21': 10, 'A31': 14, 'B11': 10, 'B21': 12, 'C11': 12, 'C21': 12, 'C31': 12, 'C41': 10, 'C51': 12, 'D1': 10, 'E1': 10, 'F1': 10,
    'A14': 16, 'A24': 16, 'A34': 20, 'B14': 16, 'B24': 20, 'C14': 10, 'C24': 10, 'C34': 8, 'C44': 8, 'C54': 10, 'D4': 8, 'E4': 8, 'F4': 8
}
//计时
function checkSession() {

    $.ajax({
        url: "../ashx/Student.ashx?Method=checkSession",
        type: "post",
        dataType: "json",
        success: function (json) {
            if (json.isOk == 1) {

            } else {
                alert(json.message);
                window.location.href = "Login.aspx";
            }
        },
        error: function () {
            alert("用户登陆过期");
            window.location.href = "Login.aspx";
        }
    });

}

//计时
function checkCode() {
    var paramData = {};
    paramData.cpid = stuObj.cpid;
    paramData.km = stuObj.mykm;
    //console.log("checkCode");
    $.ajax({
        url: "../ashx/Student.ashx?Method=checkTimeCode",
        data: paramData,
        type: "post",
        dataType: "json",
        success: function (json) {
            if (json.isOk == 1) {
                var time = json.time * 60;
                stuObj.bctime += time;
                stuObj.sec = 0;
                $('.theme-popover-mask').fadeOut(100);
                $('.theme-popover').slideUp(200);
                $("#info").html("");                 
                $("#bk").html(toHourMinute(stuObj.bctime));
                $("#yx").html(toHourMinute(stuObj.btime + stuObj.bctime));
                var sub = stuObj.sub;

                if (stuObj.mykm == 1 && (stuObj.btime + stuObj.bctime)/60 > xsobj[sub + '1'] * 60) {
                    alert("您科目一学时已满，可以进行科目二学习了！");
                    window.location.reload(true);
                    return;
                } else if (stuObj.mykm == 4 && (stuObj.btime + stuObj.bctime)/60> xsobj[sub + '4'] * 60) {
                    alert("您科目四学时已满！");
                    window.location.reload(true);
                    return;
                }
                //console.log("215");

            } else if (json.isOk == 2) {
                alert("今日学时已满，明日学时再次累计！");
                //console.log("217");
                stop();
            } else if (json.isOk == -1 && sbtime==0){
                alert(json.message);
                //console.log("224");
                restart();
            }else{
                //alert(json.message);
                //console.log("228");
                restart();
            }    
        },
        error: function () {
            //alert("学时上传失败");
            //console.log("233");
            restart()
        }
    });

}
function stop() {
    clearInterval(timer);
}
function start() {
    clearInterval(timer);
    timer = setInterval(refreshTime, 1000);
}
function restart() {
    stuObj.sec = stuObj.lastF * 5 * 60 - stuObj.btime - stuObj.bctime - 5;
    
}
var timer;
function refreshTime() {
    stuObj.sec = stuObj.sec + 1;
    var sec = stuObj.sec;
    var ss = sec % 60;
    var mi = (sec - ss) / 60;
    var sss = ss > 0 ? (ss + "秒") : ""
    //var result = (mi > 0 ? mi + "分" : "") + sss;
    $("#kc").html(toHourMinute((sec + stuObj.bctime)));
    var totaltime = stuObj.btime + stuObj.bctime + sec;
    if (stuObj.lastF < parseInt(totaltime / (5 * 60))) {
        stuObj.lastF = parseInt(totaltime / (5 * 60));
        if (totaltime % (15 * 60) == 0) {
            pz();
        } else {
            checkCode();
        }
        
    } else if (totaltime > 0 && parseInt(totaltime % (5 * 60)) == 0) {
        checkCode();
    }
    if (sec%60==0) {
        checkSession();
    }
}