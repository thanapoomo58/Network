import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { HttpClient } from '@angular/common/http';

@IonicPage()
@Component({
  selector: 'page-main',
  templateUrl: 'main.html',
})
export class MainPage {

  studentid:any;

  constructor(public navCtrl: NavController, public navParams: NavParams,public http:HttpClient) {
  }

  ionViewDidLoad() {
    this.httpFunction()
  }


  httpFunction(){
    let item = {
      studentid : "58364272"
    };
    this.http.post("http://192.168.56.2:5000/api/studentcode_to_binary",item).subscribe(response => {
      this.studentid = response['studentid'];
      console.log(this.studentid);
    },err => {
      console.log(err);
    })

  }
}
