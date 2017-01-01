import {Component, OnInit} from '@angular/core'
import { Router } from '@angular/router';

import { Project } from './project'
import {ProjectService} from "./project.service";


@Component({
    selector: 'project-list',
    templateUrl: 'static/app/projects/project-list.component.html',
    styleUrls: [
        'static/app/projects/project-list.component.css'
    ]
})
export class ProjectListComponent implements OnInit{
    projects: Project[];
    selectedProject: Project;

    constructor(
        private router: Router,
        private projectService: ProjectService) { }

    ngOnInit(): void {
        this.projectService.getProjects().then(projects => this.projects = projects);
    }

    onSelect(project: Project): void {
        this.selectedProject = project;
    }

    isSelected(project: Project): boolean {
        return this.selectedProject == project
    }
}