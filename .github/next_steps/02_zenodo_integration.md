---
title: 'Next step: Enable Zenodo integration'
---

By enabling Zenodo integration, your package will automatically get a DOI which can be used to cite your package. After enabling Zenodo integration for your GitHub repository, Zenodo will create a snapshot and archive each release you make on GitHub. Moreover, Zenodo will create a new DOI for each GitHub release of your code.

To enable Zenodo integration:

1. Go to http://zenodo.org and login with your GitHub account. When you are redirected to GitHub, *Authorize application* to give permission to Zenodo to access your account.
1. Go to <https://zenodo.org/account/settings/github/> and enable Zenodo integration of your repository by clinking on `On` toggle button.
1. Your package will get a DOI only after you make a release. Create a new release on <{{cookiecutter.repository}}/releases/new>
1. At this point you should have a DOI. To find out the DOI generated by Zenodo:
   1. Visit https://zenodo.org/deposit and click on your repository link
   1. You will find the DOI on the right column (gray-blue badge)
   1. Click on the badge and copy the **Markdown** badge link
1. Update the badge in your repository
   1. Edit README.md and replace the badge placeholder with the badge link you copied in previous setep.
   The badge placeholder is hown below.

      `[![DOI](https://zenodo.org/badge/DOI/<replace-with-created-DOI>.svg)](https://doi.org/<replace-with-created-DOI>)`

For FAQ about Zenodo please visit <https://help.zenodo.org/>.