# Generated by Django 3.1 on 2020-08-24 19:46

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('letter_tracking', '0040_auto_20200823_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='cosigners',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Larson John', 'Larson John'), ('DeLauro Rosa', 'DeLauro Rosa'), ('Himes Jim', 'Himes Jim'), ('Hayes Jahana', 'Hayes Jahana'), ('Courtney Joe', 'Courtney Joe'), ('Pingree Chellie', 'Pingree Chellie'), ('Golden Jared', 'Golden Jared'), ('Neal Richie', 'Neal Richie'), ('Trahan Lori', 'Trahan Lori'), ('Clark Katherine', 'Clark Katherine'), ('Kennedy Joe', 'Kennedy Joe'), ('Pressley Ayanna', 'Pressley Ayanna'), ('McGovern Jim', 'McGovern Jim'), ('Keating Bill', 'Keating Bill'), ('Moulton Seth', 'Moulton Seth'), ('Lynch Stephen', 'Lynch Stephen'), ('Pappas Chris', 'Pappas Chris'), ('Kuster Annie', 'Kuster Annie'), ('Cicilline David', 'Cicilline David'), ('Langevin Jim', 'Langevin Jim'), ('Welch Peter', 'Welch Peter'), ('Norcross Donald', 'Norcross Donald'), ('Kim Andy', 'Kim Andy'), ('Payne Donald', 'Payne Donald'), ('Smith Chris', 'Smith Chris'), ('Gottheimer Josh', 'Gottheimer Josh'), ('Malinowski Tom', 'Malinowski Tom'), ('Van Drew Jeff', 'Van Drew Jeff'), ('Pascrell Bill', 'Pascrell Bill'), ('Sherrill Mikie', 'Sherrill Mikie'), ('Pallone Frank', 'Pallone Frank'), ('Coleman Bonnie Watson', 'Coleman Bonnie Watson'), ('Sires Albio', 'Sires Albio'), ('Zeldin Lee', 'Zeldin Lee'), ('Velázquez Nydia', 'Velázquez Nydia'), ('Jacobs Chris', 'Jacobs Chris'), ('Lowey Nita', 'Lowey Nita'), ('Ocasio-Cortez Alexandria', 'Ocasio-Cortez Alexandria'), ('Meng Grace', 'Meng Grace'), ('Meeks Gregory', 'Meeks Gregory'), ('Katko John', 'Katko John'), ('Engel Eliot', 'Engel Eliot'), ('Rose Max', 'Rose Max'), ('Serrano José', 'Serrano José'), ('Reed Tom', 'Reed Tom'), ('Jeffries Hakeem', 'Jeffries Hakeem'), ('Maloney Carolyn', 'Maloney Carolyn'), ('Maloney Sean Patrick', 'Maloney Sean Patrick'), ('King Pete', 'King Pete'), ('Tonko Paul', 'Tonko Paul'), ('Morelle Joe', 'Morelle Joe'), ('Suozzi Tom', 'Suozzi Tom'), ('Stefanik Elise', 'Stefanik Elise'), ('Nadler Jerry', 'Nadler Jerry'), ('Rice Kathleen', 'Rice Kathleen'), ('Espaillat Adriano', 'Espaillat Adriano'), ('Higgins Brian', 'Higgins Brian'), ('Brindisi Anthony', 'Brindisi Anthony'), ('Clarke Yvette', 'Clarke Yvette'), ('Delgado Antonio', 'Delgado Antonio'), ('Fitzpatrick Brian', 'Fitzpatrick Brian'), ('Doyle Mike', 'Doyle Mike'), ('Wild Susan', 'Wild Susan'), ('Boyle Brendan', 'Boyle Brendan'), ('Lamb Conor', 'Lamb Conor'), ('Reschenthaler Guy', 'Reschenthaler Guy'), ('Houlahan Chrissy', 'Houlahan Chrissy'), ('Evans Dwight', 'Evans Dwight'), ('Perry Scott', 'Perry Scott'), ('Dean Madeleine', 'Dean Madeleine'), ('Scanlon Mary Gay', 'Scanlon Mary Gay'), ('Kelly Mike', 'Kelly Mike'), ('Joyce John', 'Joyce John'), ('Smucker Lloyd', 'Smucker Lloyd'), ('Meuser Dan', 'Meuser Dan'), ('Thompson Glenn', 'Thompson Glenn'), ('Keller Fred', 'Keller Fred'), ('Cartwright Matt', 'Cartwright Matt'), ('Rush Bobby', 'Rush Bobby'), ('LaHood Darin', 'LaHood Darin'), ('Davis Danny', 'Davis Danny'), ('Kelly Robin', 'Kelly Robin'), ('Underwood Lauren', 'Underwood Lauren'), ('Quigley Mike', 'Quigley Mike'), ('Kinzinger Adam', 'Kinzinger Adam'), ('Davis Rodney', 'Davis Rodney'), ('Bustos Cheri', 'Bustos Cheri'), ('Casten Sean', 'Casten Sean'), ('Lipinski Dan', 'Lipinski Dan'), ('Schneider Brad', 'Schneider Brad'), ('Garcia Chuy', 'Garcia Chuy'), ('Foster Bill', 'Foster Bill'), ('Schakowsky Jan', 'Schakowsky Jan'), ('Shimkus John', 'Shimkus John'), ('Bost Mike', 'Bost Mike'), ('Krishnamoorthi Raja', 'Krishnamoorthi Raja'), ('Walorski Jackie', 'Walorski Jackie'), ('Hollingsworth Trey', 'Hollingsworth Trey'), ('Pence Greg', 'Pence Greg'), ('Bucshon Larry', 'Bucshon Larry'), ('Visclosky Pete', 'Visclosky Pete'), ('Banks Jim', 'Banks Jim'), ('Brooks Susan', 'Brooks Susan'), ('Baird Jim', 'Baird Jim'), ('Carson André', 'Carson André'), ('Bergman Jack', 'Bergman Jack'), ('Walberg Tim', 'Walberg Tim'), ('Huizenga Bill', 'Huizenga Bill'), ('Upton Fred', 'Upton Fred'), ('Lawrence Brenda', 'Lawrence Brenda'), ('Amash Justin', 'Amash Justin'), ('Mitchell Paul', 'Mitchell Paul'), ('Kildee Dan', 'Kildee Dan'), ('Moolenaar John', 'Moolenaar John'), ('Tlaib Rashida', 'Tlaib Rashida'), ('Stevens Haley', 'Stevens Haley'), ('Levin Andy', 'Levin Andy'), ('Dingell Debbie', 'Dingell Debbie'), ('Slotkin Elissa', 'Slotkin Elissa'), ('Chabot Steve', 'Chabot Steve'), ('Gibbs Bob', 'Gibbs Bob'), ('Wenstrup Brad', 'Wenstrup Brad'), ('Joyce David', 'Joyce David'), ('Johnson Bill', 'Johnson Bill'), ('Beatty Joyce', 'Beatty Joyce'), ('Turner Mike', 'Turner Mike'), ('Jordan Jim', 'Jordan Jim'), ('Latta Bob', 'Latta Bob'), ('Gonzalez Anthony', 'Gonzalez Anthony'), ('Ryan Tim', 'Ryan Tim'), ('Stivers Steve', 'Stivers Steve'), ('Fudge Marcia', 'Fudge Marcia'), ('Kaptur Marcy', 'Kaptur Marcy'), ('Davidson Warren', 'Davidson Warren'), ('Balderson Troy', 'Balderson Troy'), ('Steil Bryan', 'Steil Bryan'), ('Kind Ron', 'Kind Ron'), ('Moore Gwen', 'Moore Gwen'), ('Sensenbrenner Jim', 'Sensenbrenner Jim'), ('Tiffany Tom', 'Tiffany Tom'), ('Pocan Mark', 'Pocan Mark'), ('Grothman Glenn', 'Grothman Glenn'), ('Gallagher Mike', 'Gallagher Mike'), ('Finkenauer Abby', 'Finkenauer Abby'), ('King Steve', 'King Steve'), ('Loebsack Dave', 'Loebsack Dave'), ('Axne Cindy', 'Axne Cindy'), ('Marshall Roger', 'Marshall Roger'), ('Davids Sharice', 'Davids Sharice'), ('Estes Ron', 'Estes Ron'), ('Watkins Steve', 'Watkins Steve'), ('Peterson Collin', 'Peterson Collin'), ('Craig Angie', 'Craig Angie'), ('Emmer Tom', 'Emmer Tom'), ('Stauber Pete', 'Stauber Pete'), ('Hagedorn Jim', 'Hagedorn Jim'), ('Phillips Dean', 'Phillips Dean'), ('McCollum Betty', 'McCollum Betty'), ('Omar Ilhan', 'Omar Ilhan'), ('Clay Lacy', 'Clay Lacy'), ('Luetkemeyer Blaine', 'Luetkemeyer Blaine'), ('Cleaver Emanuel', 'Cleaver Emanuel'), ('Hartzler Vicky', 'Hartzler Vicky'), ('Long Billy', 'Long Billy'), ('Wagner Ann', 'Wagner Ann'), ('Graves Sam', 'Graves Sam'), ('Smith Jason', 'Smith Jason'), ('Fortenberry Jeff', 'Fortenberry Jeff'), ('Smith Adrian', 'Smith Adrian'), ('Bacon Don', 'Bacon Don'), ('Armstrong Kelly', 'Armstrong Kelly'), ('Johnson Dusty', 'Johnson Dusty'), ('Blunt Rochester Lisa', 'Blunt Rochester Lisa'), ('Holmes Norton Eleanor', 'Holmes Norton Eleanor'), ('Crist Charlie', 'Crist Charlie'), ('Mucarsel-Powell Debbie', 'Mucarsel-Powell Debbie'), ('Deutch Ted', 'Deutch Ted'), ('Soto Darren', 'Soto Darren'), ('Rooney Francis', 'Rooney Francis'), ('Gaetz Matt', 'Gaetz Matt'), ('Murphy Stephanie', 'Murphy Stephanie'), ('Shalala Donna', 'Shalala Donna'), ('Steube Greg', 'Steube Greg'), ('Waltz Michael', 'Waltz Michael'), ('Castor Kathy', 'Castor Kathy'), ('Lawson Al', 'Lawson Al'), ('Wilson Frederica', 'Wilson Frederica'), ('Buchanan Vern', 'Buchanan Vern'), ('Webster Daniel', 'Webster Daniel'), ('Spano Ross', 'Spano Ross'), ('Wasserman Schultz Debbie', 'Wasserman Schultz Debbie'), ('Posey Bill', 'Posey Bill'), ('Bilirakis Gus', 'Bilirakis Gus'), ('Mast Brian', 'Mast Brian'), ('Dunn Neal', 'Dunn Neal'), ('Hastings Alcee', 'Hastings Alcee'), ('Diaz-Balart Mario', 'Diaz-Balart Mario'), ('Frankel Lois', 'Frankel Lois'), ('Yoho Ted', 'Yoho Ted'), ('Demings Val', 'Demings Val'), ('Rutherford John', 'Rutherford John'), ('Ferguson Drew', 'Ferguson Drew'), ('Hice Jody', 'Hice Jody'), ('Johnson Hank', 'Johnson Hank'), ('Lewis John', 'Lewis John'), ('Scott David', 'Scott David'), ('Collins Doug', 'Collins Doug'), ('Woodall Rob', 'Woodall Rob'), ('Bishop Sanford', 'Bishop Sanford'), ('McBath Lucy', 'McBath Lucy'), ('Graves Tom', 'Graves Tom'), ('Carter Buddy', 'Carter Buddy'), ('Loudermilk Barry', 'Loudermilk Barry'), ('Allen Rick', 'Allen Rick'), ('Scott Austin', 'Scott Austin'), ('Harris Andy', 'Harris Andy'), ('Sarbanes John', 'Sarbanes John'), ('Brown Anthony', 'Brown Anthony'), ('Hoyer Steny', 'Hoyer Steny'), ('Mfume Kweisi', 'Mfume Kweisi'), ('Ruppersberger Dutch', 'Ruppersberger Dutch'), ('Trone David', 'Trone David'), ('Raskin Jamie', 'Raskin Jamie'), ('Butterfield G.K.', 'Butterfield G.K.'), ('Rouzer David', 'Rouzer David'), ('Holding George', 'Holding George'), ('Walker Mark', 'Walker Mark'), ('Murphy Greg', 'Murphy Greg'), ('McHenry Patrick', 'McHenry Patrick'), ('Price David', 'Price David'), ('Foxx Virginia', 'Foxx Virginia'), ('Budd Ted', 'Budd Ted'), ('Meadows (resigned) Mark', 'Meadows (resigned) Mark'), ('Bishop Dan', 'Bishop Dan'), ('Hudson Richard', 'Hudson Richard'), ('Adams Alma', 'Adams Alma'), ('Cunningham Joe', 'Cunningham Joe'), ('Duncan Jeff', 'Duncan Jeff'), ('Timmons William', 'Timmons William'), ('Norman Ralph', 'Norman Ralph'), ('Rice Tom', 'Rice Tom'), ('Wilson Joe', 'Wilson Joe'), ('Clyburn Jim', 'Clyburn Jim'), ('Wittman Rob', 'Wittman Rob'), ('Scott Bobby', 'Scott Bobby'), ('Wexton Jennifer', 'Wexton Jennifer'), ('Riggleman Denver', 'Riggleman Denver'), ('McEachin Donald', 'McEachin Donald'), ('Spanberger Abigail', 'Spanberger Abigail'), ('Luria Elaine', 'Luria Elaine'), ('Connolly Gerry', 'Connolly Gerry'), ('Griffith Morgan', 'Griffith Morgan'), ('Cline Ben', 'Cline Ben'), ('Beyer Don', 'Beyer Don'), ('McKinley David', 'McKinley David'), ('Miller Carol', 'Miller Carol'), ('Mooney Alex', 'Mooney Alex'), ('Byrne Bradley', 'Byrne Bradley'), ('Rogers Mike', 'Rogers Mike'), ('Brooks Mo', 'Brooks Mo'), ('Aderholt Robert', 'Aderholt Robert'), ('Sewell Terri', 'Sewell Terri'), ('Roby Martha', 'Roby Martha'), ('Palmer Gary', 'Palmer Gary'), ('Guthrie Brett', 'Guthrie Brett'), ('Barr Andy', 'Barr Andy'), ('Comer James', 'Comer James'), ('Yarmuth John', 'Yarmuth John'), ('Rogers Hal', 'Rogers Hal'), ('Massie Thomas', 'Massie Thomas'), ('Kelly Trent', 'Kelly Trent'), ('Guest Michael', 'Guest Michael'), ('Palazzo Steven', 'Palazzo Steven'), ('Thompson Bennie', 'Thompson Bennie'), ('Roe Phil', 'Roe Phil'), ('Fleischmann Chuck', 'Fleischmann Chuck'), ('Cooper Jim', 'Cooper Jim'), ('DesJarlais Scott', 'DesJarlais Scott'), ('Green Mark', 'Green Mark'), ('Burchett Tim', 'Burchett Tim'), ('Kustoff David', 'Kustoff David'), ('Cohen Steve', 'Cohen Steve'), ('Rose John', 'Rose John'), ('Crawford Rick', 'Crawford Rick'), ('Womack Steve', 'Womack Steve'), ('Westerman Bruce', 'Westerman Bruce'), ('Hill French', 'Hill French'), ('Johnson Mike', 'Johnson Mike'), ('Richmond Cedric', 'Richmond Cedric'), ('Graves Garret', 'Graves Garret'), ('Scalise Steve', 'Scalise Steve'), ('Higgins Clay', 'Higgins Clay'), ('Abraham Ralph', 'Abraham Ralph'), ('Hern Kevin', 'Hern Kevin'), ('Lucas Frank', 'Lucas Frank'), ('Horn Kendra', 'Horn Kendra'), ('Cole Tom', 'Cole Tom'), ('Mullin Markwayne', 'Mullin Markwayne'), ('Cuellar Henry', 'Cuellar Henry'), ('Gohmert Louie', 'Gohmert Louie'), ('Garcia Sylvia', 'Garcia Sylvia'), ('Fletcher Lizzie', 'Fletcher Lizzie'), ('Cloud Michael', 'Cloud Michael'), ('Wright Ron', 'Wright Ron'), ('Flores Bill', 'Flores Bill'), ('Weber Randy', 'Weber Randy'), ('Babin Brian', 'Babin Brian'), ('Gooden Lance', 'Gooden Lance'), ('Escobar Veronica', 'Escobar Veronica'), ('Marchant Kenny', 'Marchant Kenny'), ('Veasey Marc', 'Veasey Marc'), ('Conaway Mike', 'Conaway Mike'), ('González Vicente', 'González Vicente'), ('Hurd Will', 'Hurd Will'), ('Granger Kay', 'Granger Kay'), ('Brady Kevin', 'Brady Kevin'), ('Vela Filemon', 'Vela Filemon'), ('Johnson Eddie Bernice', 'Johnson Eddie Bernice'), ('Lee Shelia Jackson', 'Lee Shelia Jackson'), ('Crenshaw Dan', 'Crenshaw Dan'), ('Castro Joaquin', 'Castro Joaquin'), ('Carter John', 'Carter John'), ('Williams Roger', 'Williams Roger'), ('Allred Colin', 'Allred Colin'), ('Roy Chip', 'Roy Chip'), ('Taylor Van', 'Taylor Van'), ('McCaul Michael', 'McCaul Michael'), ('Ratcliffe (resigned) John', 'Ratcliffe (resigned) John'), ('Doggett Lloyd', 'Doggett Lloyd'), ('Thornberry Mac', 'Thornberry Mac'), ('Burgess Michael', 'Burgess Michael'), ('Olson Pete', 'Olson Pete'), ('Green Al', 'Green Al'), ('Arrington Jodey', 'Arrington Jodey'), ("O'Halleran Tom", "O'Halleran Tom"), ('Grijalva Raúl', 'Grijalva Raúl'), ('Biggs Andy', 'Biggs Andy'), ('Gosar Paul', 'Gosar Paul'), ('Gallego Ruben', 'Gallego Ruben'), ('Kirkpatrick Ann', 'Kirkpatrick Ann'), ('Stanton Greg', 'Stanton Greg'), ('Schweikert David', 'Schweikert David'), ('Lesko Debbie', 'Lesko Debbie'), ('DeGette Diana', 'DeGette Diana'), ('Tipton Scott', 'Tipton Scott'), ('Lamborn Doug', 'Lamborn Doug'), ('Buck Ken', 'Buck Ken'), ('Perlmutter Ed', 'Perlmutter Ed'), ('Neguse Joe', 'Neguse Joe'), ('Crow Jason', 'Crow Jason'), ('Fulcher Russ', 'Fulcher Russ'), ('Simpson Mike', 'Simpson Mike'), ('Gianforte Greg', 'Gianforte Greg'), ('Titus Dina', 'Titus Dina'), ('Lee Susie', 'Lee Susie'), ('Horsford Steven', 'Horsford Steven'), ('Amodei Mark', 'Amodei Mark'), ('Haaland Deb', 'Haaland Deb'), ('Luján Ben Ray', 'Luján Ben Ray'), ('Torres Small Xochitl', 'Torres Small Xochitl'), ('Bishop Rob', 'Bishop Rob'), ('Curtis John', 'Curtis John'), ('McAdams Ben', 'McAdams Ben'), ('Stewart Chris', 'Stewart Chris'), ('Cheney Liz', 'Cheney Liz'), ('Young Don', 'Young Don'), ('Ruiz Raul', 'Ruiz Raul'), ('Costa Jim', 'Costa Jim'), ('Correa Lou', 'Correa Lou'), ('Bass Karen', 'Bass Karen'), ('Lieu Ted', 'Lieu Ted'), ('Swalwell Eric', 'Swalwell Eric'), ('Davis Susan', 'Davis Susan'), ('Lowenthal Alan', 'Lowenthal Alan'), ('Aguilar Pete', 'Aguilar Pete'), ('Garamendi John', 'Garamendi John'), ('Cox T.J.', 'Cox T.J.'), ('Rouda Harley', 'Rouda Harley'), ('Harder Josh', 'Harder Josh'), ('Gomez Jimmy', 'Gomez Jimmy'), ('Peters Scott', 'Peters Scott'), ('Sherman Brad', 'Sherman Brad'), ('Eshoo Anna', 'Eshoo Anna'), ('Panetta Jimmy', 'Panetta Jimmy'), ('Calvert Ken', 'Calvert Ken'), ('Garcia Mike', 'Garcia Mike'), ('Napolitano Grace', 'Napolitano Grace'), ('Waters Maxine', 'Waters Maxine'), ('Torres Norma', 'Torres Norma'), ('Lee Barbara', 'Lee Barbara'), ('Brownley Julia', 'Brownley Julia'), ('Barragan Nanette', 'Barragan Nanette'), ('Lofgren Zoe', 'Lofgren Zoe'), ('Levin Mike', 'Levin Mike'), ('Thompson Mike', 'Thompson Mike'), ('Carbajal Salud', 'Carbajal Salud'), ('Cardenas Tony', 'Cardenas Tony'), ('Bera Ami', 'Bera Ami'), ('Matsui Doris', 'Matsui Doris'), ('Cisneros Gil', 'Cisneros Gil'), ('DeSaulnier Mark', 'DeSaulnier Mark'), ('Hunter (Resigned) Duncan', 'Hunter (Resigned) Duncan'), ('McCarthy Kevin', 'McCarthy Kevin'), ('Cook Paul', 'Cook Paul'), ('Vargas Juan', 'Vargas Juan'), ('Schiff Adam', 'Schiff Adam'), ('LaMalfa Doug', 'LaMalfa Doug'), ('Roybal-Allard Lucille', 'Roybal-Allard Lucille'), ('Pelosi Nancy', 'Pelosi Nancy'), ('Porter Katie', 'Porter Katie'), ('McClintock Tom', 'McClintock Tom'), ('Nunes Devin', 'Nunes Devin'), ('McNerney Jerry', 'McNerney Jerry'), ('Takano Mark', 'Takano Mark'), ('Chu Judy', 'Chu Judy'), ('Khanna Ro', 'Khanna Ro'), ('Speier Jackie', 'Speier Jackie'), ('Huffman Jared', 'Huffman Jared'), ('Sánchez Linda', 'Sánchez Linda'), ('Case Ed', 'Case Ed'), ('Gabbard Tulsi', 'Gabbard Tulsi'), ('Bonamici Suzanne', 'Bonamici Suzanne'), ('Blumenauer Earl', 'Blumenauer Earl'), ('Schrader Kurt', 'Schrader Kurt'), ('DeFazio Peter', 'DeFazio Peter'), ('Walden Greg', 'Walden Greg'), ('DelBene Suzan', 'DelBene Suzan'), ('Beutler Jaime Herrera', 'Beutler Jaime Herrera'), ('Heck Denny', 'Heck Denny'), ('McMorris Rodgers Cathy', 'McMorris Rodgers Cathy'), ('Newhouse Dan', 'Newhouse Dan'), ('Jayapal Pramila', 'Jayapal Pramila'), ('Larsen Rick', 'Larsen Rick'), ('Smith Adam', 'Smith Adam'), ('Kilmer Derek', 'Kilmer Derek'), ('Schrier Kim', 'Schrier Kim'), ('Alexander Lamar', 'Alexander Lamar'), ('Baldwin Tammy', 'Baldwin Tammy'), ('Barrasso John', 'Barrasso John'), ('Bennet Michael', 'Bennet Michael'), ('Blackburn Marsha', 'Blackburn Marsha'), ('Blumenthal Richard', 'Blumenthal Richard'), ('Blunt Roy', 'Blunt Roy'), ('Booker Cory', 'Booker Cory'), ('Boozman John', 'Boozman John'), ('Braun Mike', 'Braun Mike'), ('Brown Sherrod', 'Brown Sherrod'), ('Burr Richard', 'Burr Richard'), ('Cantwell Maria', 'Cantwell Maria'), ('Capito Shelley', 'Capito Shelley'), ('Cardin Benjamin', 'Cardin Benjamin'), ('Carper Thomas', 'Carper Thomas'), ('Casey Bob', 'Casey Bob'), ('Cassidy Bill', 'Cassidy Bill'), ('Collins Susan', 'Collins Susan'), ('Coons Chris', 'Coons Chris'), ('Cornyn John', 'Cornyn John'), ('Cortez Masto Catherine', 'Cortez Masto Catherine'), ('Cotton Tom', 'Cotton Tom'), ('Cramer Kevin', 'Cramer Kevin'), ('Crapo Michael', 'Crapo Michael'), ('Cruz Ted', 'Cruz Ted'), ('Daines Steve', 'Daines Steve'), ('Duckworth Tammy', 'Duckworth Tammy'), ('Durbin Richard', 'Durbin Richard'), ('Enzi Michael', 'Enzi Michael'), ('Ernst Joni', 'Ernst Joni'), ('Feinstein Dianne', 'Feinstein Dianne'), ('Fischer Deb', 'Fischer Deb'), ('Gardner Cory', 'Gardner Cory'), ('Gillibrand Kirsten', 'Gillibrand Kirsten'), ('Graham Lindsey', 'Graham Lindsey'), ('Grassley Charles', 'Grassley Charles'), ('Harris Kamala', 'Harris Kamala'), ('Hassan Maggie', 'Hassan Maggie'), ('Hawley Josh', 'Hawley Josh'), ('Heinrich Martin', 'Heinrich Martin'), ('Hirono Mazie', 'Hirono Mazie'), ('Hoeven John', 'Hoeven John'), ('Hyde-Smith Cindy', 'Hyde-Smith Cindy'), ('Inhofe James', 'Inhofe James'), ('Johnson Ron', 'Johnson Ron'), ('Jones Doug', 'Jones Doug'), ('Kaine Tim', 'Kaine Tim'), ('Kennedy John', 'Kennedy John'), ('King Angus', 'King Angus'), ('Klobuchar Amy', 'Klobuchar Amy'), ('Lankford James', 'Lankford James'), ('Leahy Patrick', 'Leahy Patrick'), ('Lee Mike', 'Lee Mike'), ('Loeffler Kelly', 'Loeffler Kelly'), ('Manchin Joe', 'Manchin Joe'), ('Markey Edward', 'Markey Edward'), ('McConnell Mitch', 'McConnell Mitch'), ('McSally Martha', 'McSally Martha'), ('Menendez Bob', 'Menendez Bob'), ('Merkley Jeff', 'Merkley Jeff'), ('Moran Jerry', 'Moran Jerry'), ('Murkowski Lisa', 'Murkowski Lisa'), ('Murphy Christopher', 'Murphy Christopher'), ('Murray Patty', 'Murray Patty'), ('Paul Rand', 'Paul Rand'), ('Perdue David', 'Perdue David'), ('Peters Gary', 'Peters Gary'), ('Portman Rob', 'Portman Rob'), ('Reed Jack', 'Reed Jack'), ('Risch Jim', 'Risch Jim'), ('Roberts Pat', 'Roberts Pat'), ('Romney Mitt', 'Romney Mitt'), ('Rosen Jacky', 'Rosen Jacky'), ('Rounds Mike', 'Rounds Mike'), ('Rubio Marco', 'Rubio Marco'), ('Sanders Bernie', 'Sanders Bernie'), ('Sasse Ben', 'Sasse Ben'), ('Schatz Brian', 'Schatz Brian'), ('Schumer Charles', 'Schumer Charles'), ('Scott Rick', 'Scott Rick'), ('Scott Tim', 'Scott Tim'), ('Shaheen Jeanne', 'Shaheen Jeanne'), ('Shelby Richard', 'Shelby Richard'), ('Sinema Kyrsten', 'Sinema Kyrsten'), ('Smith Tina', 'Smith Tina'), ('Stabenow Debbie', 'Stabenow Debbie'), ('Sullivan Dan', 'Sullivan Dan'), ('Tester Jon', 'Tester Jon'), ('Thune John', 'Thune John'), ('Tillis Thom', 'Tillis Thom'), ('Toomey Patrick', 'Toomey Patrick'), ('Udall Tom', 'Udall Tom'), ('Van Hollen Chris', 'Van Hollen Chris'), ('Warner Mark', 'Warner Mark'), ('Warren Elizabeth', 'Warren Elizabeth'), ('Whitehouse Sheldon', 'Whitehouse Sheldon'), ('Wicker Roger', 'Wicker Roger'), ('Wyden Ron', 'Wyden Ron'), ('Young Todd', 'Young Todd')], default='None', max_length=7219, verbose_name='Copatrocinador/a'),
        ),
    ]