import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-estilizacao',
  templateUrl: './estilizacao.page.html',
  styleUrls: ['./estilizacao.page.scss'],
})
export class EstilizacaoPage implements OnInit {

  public itens : any = ['linha 0', 'linha 1', 'linha 2', 'linha 3', 'linha 4', 'linha 5', 'linha 6', 'linha 7', 'linha 8', 'linha 9']

  constructor() { }

  ngOnInit() {
  }

}
