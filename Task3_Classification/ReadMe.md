# Task 3 - Classification

## Brief Overview of the Whole Training Process

1. **Import Libraries:** We start by importing the required Python libraries for data processing, text preprocessing, and building the classification model.

2. **Read The Data:** The dataset containing 11,000 stories is loaded into the notebook to perform further processing.

3. **Data Preprocessing:** Several preprocessing steps are performed on the data to prepare it for the classification task:

   - **Convert The Date Type:** The date in the dataset is converted to a suitable data type for better handling and analysis.

   - **Drop ID column:** The "id" column is dropped as it does not contribute to the classification task.

   - **Remove Very Long Stories:** To avoid potential performance and memory issues, very long stories are removed from the dataset.

   - **Arabic Stopwords Removal:** Arabic stopwords (commonly used words with little semantic value) are removed to reduce noise in the data.

   - **Tashkel Removal:** Tashkeel, which represents the diacritics in Arabic text, is removed to normalize the text.

   - **Bi-Gram Tokenization:** The text is tokenized into bi-grams, capturing pairs of adjacent words. This helps the model understand word context better.

   - **Word Embedding:** The text data is transformed into a numerical representation using word embeddings, which encode semantic meaning.

   - **Label Encoding:** The categorical "Topic" labels are encoded into numerical values for training the model.

   - **Data Splitting:** The dataset is split into training and testing sets to evaluate the model's performance.

4. **Classification Deep Learning Method RNN:** We employ a Recurrent Neural Network (RNN) for the classification task using Long-Short Term memory (LSTM) layers, as it can effectively model sequential data like text.

5. **Evaluation:** The model is evaluated on both the training and test datasets to measure its performance.

6. **Trying Transformer-Based Models:** In an attempt to explore alternative approaches, I experimented with transformer-based models like BERT or GPT for text classification. However, due to time constraints and the complexity of transformer models, I could not complete the implementation before the deadline.

## Meaning of Each Result and Metric for This Specific Task

- **Precision:** Precision measures the accuracy of positive predictions made by the model. In this context, it indicates how many of the stories classified as belonging to a specific topic are genuinely relevant to that topic.

- **Recall:** Recall measures the ability of the model to identify positive instances correctly. In our scenario, it represents the proportion of stories belonging to a specific topic that were correctly classified.

- **F-score:** The F-score is the harmonic mean of precision and recall. It provides a balanced measure of the model's accuracy, taking into account both false positives and false negatives.

- **Accuracy:** Accuracy measures the overall correctness of the model's predictions, regardless of class. It is the ratio of correctly classified instances to the total instances in the dataset.

## Enhancements for Better Results

To improve the classification performance, we can consider the following enhancements:

1. **Model Architecture:** Experiment with different neural network architectures, such as Bidirectional RNNs, or GRU, to see if they capture the sequential patterns in the data better.

2. **Hyperparameter Tuning:** Optimize the hyperparameters of the model, such as learning rate, batch size, and number of hidden units, using techniques like grid search or random search.

3. **Expand Dataset from Hespress:** To enhance the model's generalization, we can collect more stories from the same news site (Hespress) from later years, spanning from 2021 to 2023. This will allow the model to learn from more recent data and adapt to potential changes in language usage and topics over time.

4. **Incorporate Data from Other News Sites:** To further improve the model's generalization and account for variations in writing styles and topics, we can consider incorporating stories from other reputable Arabic news sites.

5. **Transfer Learning:** Pretrain the word embeddings on a larger Arabic corpus or use pre-trained language models like BERT or GPT to leverage their knowledge for our classification task.
