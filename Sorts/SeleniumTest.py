from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select



def wait(driver, time = 1):
	try:
		element = WebDriverWait(driver, time).until(
		    EC.presence_of_element_located((By.ID, "userDropdown"))
		)
	except :
		print("deu bode")

def main():

	firefox = login()
	wait(firefox)

	firefox.get('http://localhost:3000/#/estudante/add')
	preencher(firefox)


#	firefox.quit()

def preencher(driver):
	
#wait
#	wait(driver, 3)
	nome = driver.find_element_by_name('nome')
	nome.send_keys('Joao da Silva')

	data_nascimento = driver.find_element_by_name('data_nascimento')
	data_nascimento.send_keys('2000-11-11')

	cpf = driver.find_element_by_name('cpf')
	cpf.send_keys('04171650305')

	rg = driver.find_element_by_name('rg')
	rg.send_keys('370043911')

	nome_pai = driver.find_element_by_name('nome_pai')
	nome_pai.send_keys('Jose da Silva')

	nome_mae = driver.find_element_by_name('nome_mae')
	nome_mae.send_keys('Maria da Silva')

	endereco = driver.find_element_by_name('endereco')
	endereco.send_keys('Rua qualquer')

	cep = driver.find_element_by_name('cep')
	cep.send_keys('60730235')

	bairro = driver.find_element_by_name('bairro')
	bairro.send_keys('Bairro qualquer')

	email = driver.find_element_by_name('email')
	email.send_keys('email@email.com')

	telefone = driver.find_element_by_name('telefone')
	telefone.send_keys('33112233')

	celular = driver.find_element_by_name('celular')
	celular.send_keys('85988880000')

	ano = driver.find_element_by_name('ano')
	ano.send_keys('2018')


	sexo = Select(driver.find_element_by_name('sexo'))
	sexo.select_by_index(1)


	estado_civil_id = Select(driver.find_element_by_name('estado_civil_id'))
	estado_civil_id.select_by_index(1)

	uf_id = Select(driver.find_element_by_name('uf_id'))
	uf_id.select_by_index(1)

	cidade_id = Select(driver.find_element_by_name('cidade_id'))
	cidade_id.select_by_index(1)

	escola_id = Select(driver.find_element_by_name('escola_id'))
	escola_id.select_by_index(1)

	grau_instrucao_id = Select(driver.find_element_by_name('grau_instrucao_id'))
	grau_instrucao_id.select_by_index(1)

	habilitacao = Select(driver.find_element_by_name('habilitacao'))
	habilitacao.select_by_index(1)

	categoria_habilitacao_id = Select(driver.find_element_by_name('categoria_habilitacao_id'))
	categoria_habilitacao_id.select_by_index(1)

	tipo_veiculo_id = Select(driver.find_element_by_name('tipo_veiculo_id'))
	tipo_veiculo_id.select_by_index(1)

	conducao_propria = Select(driver.find_element_by_name('conducao_propria'))
	conducao_propria.select_by_index(1)


	curso_id = Select(driver.find_element_by_name('curso_id'))
	curso_id.select_by_index(1)

	periodo_curso_id = Select(driver.find_element_by_name('periodo_curso_id'))
	periodo_curso_id.select_by_index(1)

	centro_estagio_id = Select(driver.find_element_by_name('centro_estagio_id'))
	centro_estagio_id.select_by_index(1)

def login(usuario = 'admin', senha = '1234'):
	firefox = webdriver.Firefox()
	firefox.get('http://localhost:3000/#/login')

	usuario = firefox.find_element_by_name('username')
	usuario.send_keys('admin')


	senha = firefox.find_element_by_name('password')
	senha.send_keys('1234')

	senha.send_keys(Keys.ENTER)
	wait = WebDriverWait(firefox, 2)

	return firefox




main()
