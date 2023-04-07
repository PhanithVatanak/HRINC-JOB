import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule, routingComponent } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { SearchJobCategoryComponent } from './components/home/search-job-category/search-job-category.component';
import { MaterialModule } from './material/material.module';
import { HomeMainJobComponent } from './components/home/home-main-job/home-main-job.component';
import { FooterComponent } from './components/footer/footer.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule } from '@angular/common/http'
import { JobsiteDataService } from './services/jobsite-data.service';



@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    SearchJobCategoryComponent,
    HomeMainJobComponent,
    FooterComponent,
    routingComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MaterialModule,
    BrowserAnimationsModule,
    HttpClientModule
  ],
  providers: [JobsiteDataService],
  bootstrap: [AppComponent]
})
export class AppModule { }
