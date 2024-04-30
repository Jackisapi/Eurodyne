import ripper_doc


def trainer():
    model = input("Please enter a model tag (hugging face) \n :> ")
    data = input("Please enter a Data tag (Directory coming soon pookie bear) \n :> ")
    output_dir = input("Please enter an output directory ")
    try:
        ripper = ripper_doc.Ripper(model_tag=model, data_tag=data, output_dir=output_dir, args='pubmed')
        ripper.prep_data()
        ripper.start_training()
    except Exception as e:
        print(f"ERROR: \n {e}")
