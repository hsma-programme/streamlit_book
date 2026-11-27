# HSMA - Web Apps with Streamlit

This book accompanies the Streamlit sessions in the [Health Service Modelling Associates (HSMA) Programme](https://hsma.co.uk/).

You can view the book at: **<https://webapps.hsma.co.uk/>**

![](book/assets/images/cover_image_robot.jpeg)

<br>

## Contributing and sharing feedback

Please open an issue if you spot an error, or have suggestions for improvements or additional chapters.

## Viewing the book locally

The book is available [online](https://webapps.hsma.co.uk/). To build it locally, you will need to:

1. Clone this repository.
2. Ensure you have Quarto installed.
3. Create the virtual environment - for example, using mamba:

```bash
mamba create -n "streamlit_book" python=3.14
mamba activate streamlit_book
pip install -r requirements.txt
```

4. Use the following commands to build and preview the book:

```bash
quarto render book
quarto preview book
```

## Citation

Please cite this book as:

> [Sammi Rosser](https://github.com/Bergam0t) [![ORCID ID](book/assets/images/orcid.png)](https://orcid.org/0000-0002-9552-8988) and [Amy Heather](https://github.com/amyheather) [![ORCID ID](book/assets/images/orcid.png)](https://orcid.org/0000-0002-6596-3479). **HSMA - Web Apps with Streamlit**. <https://webapps.hsma.co.uk/>.

A `CITATION.cff` file is also provided.
