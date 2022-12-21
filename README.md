<h1>COVID PREDICTION</h1>
<h2>Prediction of Covid using AIML algorithms</h2>
<h2>Steps involved in doing this process</h2>
<p>After importing files using pandas ,the following steps are performed</p>
<ul type="disk">
  <li><dl>
      <dt>Cleaning the data</dt>
      <dd>Checking if there are any non data-type in the respective columns of the csv file.Then ,all the missing values of the dataset are filled with statistical elements like mean ,median or most frequently occurred value.</dd>
      </dl>
  </li>
  <li><dl>
      <dt>Encoding the object type data</dt>
      <dd>Since ,machine cannot understand human language ,it must be converted to numericals.This is achieved through labelEncoding(2),OneHotEncoding(>2) etc.This is the main phase in preprocessing.</dd>
      </dl>
  </li>
  <li><dl>
      <dt>Splitting the data for training the model</dt>
      <dd>To train the model so that it can predict the result of user data ,we have to do this process .The entire dataset is splitted in 4 : 1 ratio.</dd>
      </dl>
  </li>
  <li><dl>
      <dt>Applying various algorithms</dt>
      <dd>Various machine learning algorithms like random forest ,RF with MCC , XGBoost ,NaiveBayes ,Decision tree ,logistic Regression etc are applied.For different algorithms we got different score and precision.</dd>
      </dl>
  </li>
  <li><dl>
      <dt>Building pickel file</dt>
      <dd>After comparing all algorithms ,we can choose the best fitted process and convert it to a model.This model is built into a pickle file using python modules  again ,and save to storage</dd>
      </dl></li>
  <li><dl>
      <dt>Making the User Interface</dt>
      <dd>We can make the UI using simple HTML and CSS or any other frameworks.We give user a space to input all the required data through input tags and retrive the response through backend functionalities.</dd>
      </dl></li>
  <li><dl>
      <dt>Retriving data and displaying result</dt>
      <dd>The request given by user is taken and given to model for processing output.The backend frameworks for python - aiml like <b>django</b> ,flask are used to complete this task.The result is again sent as response and displayed through http response.This can be deployed using various cloud services</dd>
      </dl></li>
</ul>
