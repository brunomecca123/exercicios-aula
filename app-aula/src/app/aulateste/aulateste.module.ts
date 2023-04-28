import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { AulatestePageRoutingModule } from './aulateste-routing.module';

import { AulatestePage } from './aulateste.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    AulatestePageRoutingModule
  ],
  declarations: [AulatestePage]
})
export class AulatestePageModule {}
