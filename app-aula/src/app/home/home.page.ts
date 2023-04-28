import { Component } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {
 public nomeDaVariavel: any;
 public pessoa = {
  id:1,
  nome: 'Cunha',
  sobrenome: 'Sorbas',
  gostoMusical: 'mpb',
  idade: 23
 }

public listaAlunos :any= []

  constructor() {
this.nomeDaVariavel = "objetos em ts";
this.pessoa.gostoMusical = "rock";
console.log(this.pessoa)
}

public acrescentaIdade(){
  this.pessoa.idade += 1;
}

public diminuiIdade(){
  this.pessoa.idade -= 1;
}

public addAluno(nome: String, idade: number, gostoMusical: String){
this.listaAlunos.push(
{
  nome: nome,
  idade: idade,
  gostoMusical: gostoMusical

});

this.printaListaAlunos();
}

public printaListaAlunos(){
  this.listaAlunos.forEach((element:any) => {
    console.log(element)
    if (element.idade < 25){
      console.log(element)
    } else{
      
    }
    
  });
  
}

}