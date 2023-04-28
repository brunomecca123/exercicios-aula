import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AulatestePage } from './aulateste.page';

const routes: Routes = [
  {
    path: '',
    component: AulatestePage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class AulatestePageRoutingModule {}
