import { Component, OnInit } from '@angular/core';
import { DadosService } from '../api/dados.service';

@Component({
  selector: 'app-dados',
  templateUrl: './dados.page.html',
  styleUrls: ['./dados.page.scss'],
})
export class DadosPage implements OnInit {

  constructor(private service: DadosService) { }

  public getAllDados(){
    this.service.getAllDados().then(dados => {
      console.log('GET ALL DADOS');
      console.log(dados);
    })
  }

  ngOnInit() {
  }

}
