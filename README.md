# The Dilemma
There are many tools available for data visualization, ranging from free to paid solutions and even “build your own” from scratch.

Building your own solution in a way that is flexible and functional is a challenging task. Additionally, there are maintenance and long-term costs, which should be considered when building a solution from scratch.

I will cover an approach using two open-source technologies (Metabase + Django) to create a data visualization platform that is powerful, flexible, and fully customizable.

## Part 1 — Hello, Metabase
Metabase is an open-source tool for business intelligence and data visualization and it allows us to ask “questions” (or create reports) regarding our data and display the answers in formats that make sense, being charts or detailed tables.

It’s possible to connect several data sources to Metabase (such as PostgreSQL, MySQL, Big Query, MongoDB, etc) and create reports directly from a web interface. Those reports can be written in plain SQL or created directly from the interface report building tools, without writing any code.

Metabase is an incredible tool by itself and the part we will cover in this article will be the Embedded Reports. 

Embedded reports can be added or embedded to any application outside of Metabase, making them a great option to include in your own custom applications without having to build them from scratch.

## Part 2 — Preparing Django to Integrate with Metabase
Django is a very flexible python web framework and allows us to create Rest APIs and/or web pages very easily.

Since we can embed Metabase reports into our applications, we just need a way to connect the dots.

To do so, we’ll use Django to save and display Metabase report links.

### Required Models
We’ll initially need these two database entities:

#### `ReportEngine`
Represents the tool responsible for creating the report links. At this moment, it will only be Metabase, but in the future other tools can be added painlessly.

#### `EmbeddedReport`
The Metabase report itself. Here we need to know the report type i.e. if the report is a single Metabase question or a dashboard.# Django-Metabase
