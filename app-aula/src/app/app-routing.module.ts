import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: 'home',
    loadChildren: () => import('./home/home.module').then( m => m.HomePageModule)
  },
  {
    path: '',
    redirectTo: 'home',
    pathMatch: 'full'
  },
  {
    path: 'grid1',
    loadChildren: () => import('./grid1/grid1.module').then( m => m.Grid1PageModule)
  },
  {
    path: 'grid2',
    loadChildren: () => import('./grid2/grid2.module').then( m => m.Grid2PageModule)
  },
  {
    path: 'form',
    loadChildren: () => import('./form/form.module').then( m => m.FormPageModule)
  },
  {
    path: 'form2',
    loadChildren: () => import('./form2/form2.module').then( m => m.Form2PageModule)
  },
  {
    path: 'ngpage',
    loadChildren: () => import('./ngpage/ngpage.module').then( m => m.NgpagePageModule)
  },
  {
    path: 'filme',
    loadChildren: () => import('./filme/filme.module').then( m => m.FilmePageModule)
  },
  {
    path: 'estilizacao',
    loadChildren: () => import('./estilizacao/estilizacao.module').then( m => m.EstilizacaoPageModule)
  },
  {
    path: 'aulateste',
    loadChildren: () => import('./aulateste/aulateste.module').then( m => m.AulatestePageModule)
  },
  {
    path: 'detalhefilme',
    loadChildren: () => import('./detalhefilme/detalhefilme.module').then( m => m.DetalhefilmePageModule)
  },
  {
    path: 'dados',
    loadChildren: () => import('./dados/dados.module').then( m => m.DadosPageModule)
  },
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
