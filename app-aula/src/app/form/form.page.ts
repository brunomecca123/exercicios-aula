import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-form',
  templateUrl: './form.page.html',
  styleUrls: ['./form.page.scss'],
})
export class FormPage implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  public primeiroMetodo(){
  console.log("xurumelas");
  }

  public segundoMetodo(){
    console.log("xablau");
  }
}
