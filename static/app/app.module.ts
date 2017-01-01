import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';

import { AppComponent }  from './app.component';
import { ProjectListComponent } from './projects/project-list.component'
import { ProjectService } from "./projects/project.service";

import { AppRoutingModule }     from './app-routing.module';
import { PageNotFoundComponent } from "./pages/not-found.component";


@NgModule({
    imports: [
        BrowserModule,
        FormsModule,
        AppRoutingModule
    ],
    declarations: [
        AppComponent,
        ProjectListComponent,
        PageNotFoundComponent
    ],
    providers: [
        ProjectService
    ],
    bootstrap: [ AppComponent ]
})
export class AppModule { }
