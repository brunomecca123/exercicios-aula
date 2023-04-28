import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-detalhefilme',
  templateUrl: './detalhefilme.page.html',
  styleUrls: ['./detalhefilme.page.scss'],
})
export class DetalhefilmePage implements OnInit {

  public nomedapaginaproduto = {
    codigo : 0,
    titulo: '',
    sinopse: '',
    ano: 0,
    status: false,
    visible: false,
    adicionado: false 
  }

  constructor(private route: ActivatedRoute) {
    this.route.queryParams.subscribe(params=>{
      this.nomedapaginaproduto = params['nomedapaginaproduto']
    });
   }

  ngOnInit() {
  }

}
