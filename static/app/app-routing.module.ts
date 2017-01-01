import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { ProjectListComponent }  from './projects/project-list.component';
import { PageNotFoundComponent } from "./pages/not-found.component";

const routes: Routes = [
    { path: '', redirectTo: '/projects', pathMatch: 'full' },
    { path: 'projects',  component: ProjectListComponent },
    { path: '**', component: PageNotFoundComponent}
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
