import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { HttpClient } from '@angular/common/http';

@IonicPage()
@Component({
  selector: 'page-main',
  templateUrl: 'main.html',
})
export class MainPage {

  studentcode:any;

  constructor(public navCtrl: NavController, public navParams: NavParams,public http:HttpClient) {
  }

  ionViewDidLoad() {
    this.httpFunction()
  }


  httpFunction(){
    let item = {
      studentcode : "58364609"
    };
    this.http.post("http://192.168.56.2:5000/api/studentcode-to-binary",item).subscribe(response => {
      this.studentcode = response['studentcode'];
      console.log(this.studentcode);
    },err => {
      console.log(err);
    })

  }
}
