import {Component} from '@angular/core';

@Component({
    selector: 'trs-app',
    template: `
        <h1>{{title}}</h1>
        <nav>
          <a routerLink="/projects" routerLinkActive="active">Projects</a>
        </nav>
        <router-outlet></router-outlet>
      `,
    styleUrls: ['static/app/app.component.css']
})
export class AppComponent {
    title = 'My projects'
}