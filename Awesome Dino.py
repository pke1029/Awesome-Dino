import pygame
import math


class Page:

	def __init__(self, image, button_list, bgm=True, se=None):
		self.image = image
		self.button_list = button_list
		self.bgm = bgm
		self.se = se

	def show(self, screen):
		screen.blit(self.image, (0, 0))

	def make_current(self):
		global current_page
		current_page = self
		if self.se is not None:
			pygame.mixer.Sound.play(self.se)
		if self.bgm is True:
			if pygame.mixer.music.get_busy() == 0:
				pygame.mixer.music.unpause()
		else:
			pygame.mixer.music.pause()


class Button:

	def __init__(self, region=[200, 150, 600, 450]):
		self.region = region						# [x1, y1, x2, y2]
		self.surf = self.surf()

	def surf(self):
		width = self.region[2] - self.region[0]
		height = self.region[3] - self.region[1]
		surface = pygame.Surface((width, height), pygame.SRCALPHA)
		surface.fill((0, 128, 255, 50))
		return surface

	def press(self):
		self.target_page.make_current()

	def glow(self, screen):
		x, y = self.region[0], self.region[1]
		screen.blit(self.surf, (x, y))


class Bullet:

	def __init__(self):
		self.x_pos = 0
		self.y_pos = 0
		self.speed = 7
		self.in_use = False

	def shoot(self, hero_x, hero_y):
		self.x_pos = hero_x+16
		self.y_pos = hero_y-30
		self.in_use = True

	def move(self):
		self.y_pos -= self.speed

	def collide(self):
		self.in_use = False


class Boss_bullet:

	def __init__(self):
		self.x_pos = 390
		self.y_pos = 140
		self.x_speed = 0
		self.y_speed = 0
		self.in_use = False

	def shoot(self, x_des, y_des, x_init=390, y_init=140):
		self.x_pos = x_init
		self.y_pos = y_init
		a = (x_des+32) - (self.x_pos+10)
		b = (y_des+32) - (self.y_pos+10)
		c = math.sqrt(a**2 + b**2)
		self.x_speed = (7*a/c)
		self.y_speed = (7*b/c)
		self.in_use = True

	def move(self):
		self.x_pos += self.x_speed
		self.y_pos += self.y_speed

	def collide(self):
		self.in_use = False


def hero_shoot(hb_list, hero_x, hero_y, bullet_se):
	current_time = pygame.time.get_ticks()
	global last_shoot_time
	if current_time - last_shoot_time > 500:
		for bullet in hb_list:
			if bullet.in_use is False:
				bullet.shoot(hero_x, hero_y)
				pygame.mixer.Sound.play(bullet_se)
				last_shoot_time = pygame.time.get_ticks()
				break


def shoot_circle(bb_list):
	t = pygame.time.get_ticks()
	t = t/1000
	t = t % (2*math.pi)
	x_init = 390+200*math.sin(t)
	for i in range(15):
		theta = 2*math.pi*i/15 + 0.17
		x_des = math.sin(theta)*1000 + 390
		y_des = math.cos(theta)*1000 + 140
		bb_list[i].shoot(x_des, y_des, x_init=x_init)


def hell_shooter(fps, screen, clock, bullet):

	# load asset 
	space_img = pygame.image.load('data\\space.png')
	hero_img = pygame.image.load('data\\hero.png')
	boss_img = pygame.image.load('data\\boss.png')
	boss_bullet_img = pygame.image.load('data\\boss_bullet.png')
	heart_img = pygame.image.load('data\\heart.png')
	if bullet == 'sheep':
		hero_bullet_img = pygame.image.load('data\\sheep_bullet.png')
		bullet_se = pygame.mixer.Sound('data\\Farm_Morning_with_Sheep.wav')
	else:
		hero_bullet_img = pygame.image.load('data\\fire_bullet.png')
		bullet_se = pygame.mixer.Sound('data\\Big_Gun_Shots_Close.wav')

	# hero setting
	global win
	global hero_speed
	global hero_health
	hero_x = 368
	hero_y = 500
	hero_move_x = 0
	hero_move_y = 0

	# hero shoot tracking
	global last_shoot_time 
	last_shoot_time = pygame.time.get_ticks()
	hb1 = Bullet()
	hb2 = Bullet()
	hb3 = Bullet()
	hb4 = Bullet()
	hb5 = Bullet()
	hb_list = [hb1, hb2, hb3, hb4, hb5]

	# boss setting
	boss_health = 30
	boss_last_shoot_time = pygame.time.get_ticks()
	boss_last_shoot_time2 = pygame.time.get_ticks()
	boss_last_shoot_time3 = pygame.time.get_ticks()
	bb1 = Boss_bullet()
	bb2 = Boss_bullet()
	bb3 = Boss_bullet()
	bb4 = Boss_bullet()
	bb5 = Boss_bullet()
	bb6 = Boss_bullet()
	bb7 = Boss_bullet()
	bb8 = Boss_bullet()
	bb9 = Boss_bullet()
	bb10 = Boss_bullet()
	bb11 = Boss_bullet()
	bb12 = Boss_bullet()
	bb13 = Boss_bullet()
	bb14 = Boss_bullet()
	bb15 = Boss_bullet()
	bb_list = [bb1, bb2, bb3, bb4, bb5, bb6, bb7, bb8, bb9, bb10, bb11, bb12, bb13, bb14, bb15]
	bb16 = Boss_bullet()
	bb17 = Boss_bullet()
	bb18 = Boss_bullet()
	bb19 = Boss_bullet()
	bb20 = Boss_bullet()
	bb21 = Boss_bullet()
	bb22 = Boss_bullet()
	bb23 = Boss_bullet()
	bb24 = Boss_bullet()
	bb25 = Boss_bullet()
	bb26 = Boss_bullet()
	bb27 = Boss_bullet()
	bb28 = Boss_bullet()
	bb29 = Boss_bullet()
	bb30 = Boss_bullet()
	bb_list2 = [bb16, bb17, bb18, bb19, bb20, bb21, bb22, bb23, bb24, bb25, bb26, bb27, bb28, bb29, bb30]

	while boss_health > 0 and hero_health > 0:

		screen.blit(space_img, (0, 0))
		screen.blit(boss_img, (200, 50))

		event_list = pygame.event.get()
		for event in event_list:

			if event.type == pygame.QUIT:
				pygame.quit()
				quit()	

			# moving hero
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					hero_move_x += -hero_speed
				if event.key == pygame.K_RIGHT:
					hero_move_x += hero_speed
				if event.key == pygame.K_UP:
					hero_move_y += -hero_speed
				if event.key == pygame.K_DOWN:
					hero_move_y += hero_speed
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					hero_move_x += hero_speed
				if event.key == pygame.K_RIGHT:
					hero_move_x += -hero_speed
				if event.key == pygame.K_UP:
					hero_move_y += hero_speed
				if event.key == pygame.K_DOWN:
					hero_move_y += -hero_speed

			# hero shooting
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					hero_shoot(hb_list, hero_x, hero_y, bullet_se)

		# boss shooting 1
		current_time = pygame.time.get_ticks()
		if current_time - boss_last_shoot_time > 700:
			for boss_bullet in bb_list:
				if boss_bullet.in_use is False:
					boss_bullet.shoot(hero_x, hero_y)
					boss_last_shoot_time = pygame.time.get_ticks()
					break
			
		# boss shooting 2
		current_time = pygame.time.get_ticks()
		if current_time - boss_last_shoot_time2 > 3000:
			shoot_circle(bb_list2)
			boss_last_shoot_time2 = pygame.time.get_ticks()

		# boss shooting 3
		current_time = pygame.time.get_ticks()
		if current_time - boss_last_shoot_time3 > 1000:
			for boss_bullet in bb_list:
				if boss_bullet.in_use is False:
					boss_bullet.shoot(hero_x, hero_y, x_init=250, y_init=140)
					break
			for boss_bullet in bb_list:
				if boss_bullet.in_use is False:
					boss_bullet.shoot(hero_x, hero_y, x_init=530, y_init=140)
					boss_last_shoot_time3 = pygame.time.get_ticks()
					break

		# update hero position and moving boundary
		hero_x += hero_move_x
		hero_y += hero_move_y
		if hero_x < 0:
			hero_x = 0
		elif hero_x > 736:
			hero_x = 736
		if hero_y < 200:
			hero_y = 200
		elif hero_y > 536:
			hero_y = 536
		screen.blit(hero_img, (hero_x, hero_y))

		# update hero bullet position
		for bullet in hb_list:
			if bullet.in_use is True:
				bullet.move()
				if bullet.y_pos < 140 and bullet.x_pos > 170 and bullet.x_pos < 600:
					bullet.collide()
					boss_health -= 1
				elif bullet.y_pos < -30:
					bullet.collide()
				if bullet.in_use is True:
					screen.blit(hero_bullet_img, (bullet.x_pos, bullet.y_pos))

		# update boss bullet position
		for boss_bullet in bb_list + bb_list2: 
			if boss_bullet.in_use is True:
				boss_bullet.move()
				in_x = boss_bullet.x_pos+20 > hero_x+10 and boss_bullet.x_pos < hero_x+64-10
				in_y = boss_bullet.y_pos+20 > hero_y+10 and boss_bullet.y_pos < hero_y+64-10
				out_x = boss_bullet.x_pos+20 < 0 or boss_bullet.x_pos > 800 
				out_y = boss_bullet.y_pos > 600 or boss_bullet.y_pos < -20
				if in_x and in_y:
					boss_bullet.collide()
					hero_health -= 1
				elif out_x or out_y:
					boss_bullet.collide()
				if boss_bullet.in_use is True:
					screen.blit(boss_bullet_img, (boss_bullet.x_pos, boss_bullet.y_pos))

		# health indicate
		for i in range(hero_health):
			screen.blit(heart_img, (30*(i+1), 540))
		

		pygame.display.update()
		clock.tick(fps)

	if boss_health <= 0:
		win = True
	elif hero_health <= 0:
		win = False

	# reset health and speed
	hero_health = 5
	hero_speed = 3


pygame.init()


title = "Awesome Dino"
resolution = (screen_width, screen_height) = (800, 600)
fps = 30
icon = pygame.image.load('data\\icon.png')

pygame.display.set_icon(icon)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption(title)
clock = pygame.time.Clock()

# load asset
intro_img = pygame.image.load('data\\intro.png')
walk_img = pygame.image.load('data\\walk.png')
notice_img = pygame.image.load('data\\notice.png')
poster_img = pygame.image.load('data\\poster.png')
idea_img = pygame.image.load('data\\idea.png')
tue_img = pygame.image.load('data\\tuesday.png')
wed_img = pygame.image.load('data\\wednesday.png')
thur_img = pygame.image.load('data\\thursday.png')
fri_img = pygame.image.load('data\\friday.png')
sat_img = pygame.image.load('data\\saturday.png')

idle_day_img = pygame.image.load('data\\idle_day.png')
routine_img = pygame.image.load('data\\routine.png')
eat_img = pygame.image.load('data\\eat.png')
workout_img = pygame.image.load('data\\workout.png')
speed_img = pygame.image.load('data\\speed.png')
health_img = pygame.image.load('data\\health.png')
idle_night_img = pygame.image.load('data\\idle_night.png')

ev1_choice_img = pygame.image.load('data\\ev1_choice.png')
go_out_img = pygame.image.load('data\\go_out.png')
walk_choice_img = pygame.image.load('data\\walk_choice.png')
hug_bear_img = pygame.image.load('data\\hug_bear.png')
hug_img = pygame.image.load('data\\hug.png')
pet_dog_img = pygame.image.load('data\\pet_dog.png')
pet_img = pygame.image.load('data\\pet.png')

knock_img = pygame.image.load('data\\knock.png')
birthday_img = pygame.image.load('data\\birthday.png')
happy_img = pygame.image.load('data\\happy.png')

clean1_img = pygame.image.load('data\\clean1.png')
clean2_img = pygame.image.load('data\\clean2.png')

shop_img = pygame.image.load('data\\shop.png')
keeper1_img = pygame.image.load('data\\keeper1.png')
keeper2_img = pygame.image.load('data\\keeper2.png')
fire_img = pygame.image.load('data\\fire.png')
sheep_img = pygame.image.load('data\\sheep.png')

knock2_img = pygame.image.load('data\\knock2.png')
ufo_img = pygame.image.load('data\\ufo.png')
obtain_ufo_img = pygame.image.load('data\\obtain_ufo.png')
sun_img = pygame.image.load('data\\sunday.png')
instruction_img = pygame.image.load('data\\instruction.png')

dead_img = pygame.image.load('data\\dead.png')
game_over_img = pygame.image.load('data\\game_over.png')
run_img = pygame.image.load('data\\run.png')
save_img = pygame.image.load('data\\save.png')
celebrate_img = pygame.image.load('data\\celebrate.png')
credit_img = pygame.image.load('data\\credit.png')
thank_img = pygame.image.load('data\\thank.png')

eat_se = pygame.mixer.Sound('data\\Eating_And_Slurping.wav')
idea_se = pygame.mixer.Sound('data\\pluck.wav')
walk_se = pygame.mixer.Sound('data\\Flip_Flops_On_Concrete.wav')
clap_se = pygame.mixer.Sound('data\\clap.wav')
knock_se = pygame.mixer.Sound('data\\Knock_On_Wooden_Door.wav')
partyhorn_se = pygame.mixer.Sound('data\\partyhorn.wav')
panting_se = pygame.mixer.Sound('data\\Animal_Panting.wav')

pygame.mixer.music.load('data\\Bike_Sharing_to_Paradise.mp3')


# create buttons
b1_intro = Button([310, 380, 545, 450])
quit_button = Button([310, 460, 545, 530])
b1_walk = Button()
b1_notice = Button()
b1_poster = Button()
b1_idea = Button()
b1_tue = Button()
b1_idle_day = Button()
b1_routine = Button([580, 350, 775, 435])
b2_routine = Button([580, 455, 775, 565])
b1_eat = Button()
b1_workout = Button()
b1_health = Button()
b1_speed = Button()
b1_idle_night = Button()
b1_ev1_choice = Button([560, 235, 780, 395])
b2_ev1_choice = Button([560, 425, 780, 580])
b1_go_out = Button([540, 285, 765, 435])
b2_go_out = Button([540, 460, 765, 590])
b1_walk2 = Button()
b1_walk_choice = Button([45, 445, 345, 590])
b2_walk_choice = Button([375, 445, 710, 590])
b1_hug_bear = Button()
b1_hug = Button()
b1_pet_dog = Button()
b1_pet = Button()
b1_wed = Button()
b1_knock = Button()
b1_birthday = Button()
b1_happy = Button()
b1_thur = Button()
b1_clean1 = Button()
b1_clean2 = Button()
b1_fri = Button()
b1_walk3 = Button()
b1_shop = Button()
b1_keeper = Button([460, 400, 790, 475])
b2_keeper = Button([460, 500, 790, 595])
b3_keeper1 = Button([390, 90, 475, 155])
b3_keeper2 = Button([330, 90, 475, 155])
b1_fire = Button()
b1_sheep = Button()
b1_sat = Button()
b1_knock2 = Button()
b1_ufo = Button()
b1_obtain_ufo = Button()
b1_sun = Button()
b1_instruction = Button()
b1_dead = Button()
b1_game_over = Button()
b1_run = Button()
b1_save = Button()
b1_celebrate = Button()
b1_credit = Button()
b1_thank = Button()

# create pages
intro_page = Page(intro_img, [b1_intro, quit_button])
walk_page = Page(walk_img, [b1_walk], se=walk_se)
notice_page = Page(notice_img, [b1_notice])
poster_page = Page(poster_img, [b1_poster])
idea_page = Page(idea_img, [b1_idea], se=idea_se)
tue_page = Page(tue_img, [b1_tue])

idle_day_page = Page(idle_day_img, [b1_idle_day])
routine_page = Page(routine_img, [b1_routine, b2_routine])
eat_page = Page(eat_img, [b1_eat], se=eat_se)
workout_page = Page(workout_img, [b1_workout])
health_page = Page(health_img, [b1_health])
speed_page = Page(speed_img, [b1_speed])
idle_night_page = Page(idle_night_img, [b1_idle_night])

ev1_choice_page = Page(ev1_choice_img, [b1_ev1_choice, b2_ev1_choice])
go_out_page = Page(go_out_img, [b1_go_out, b2_go_out])
walk2_page = Page(walk_img, [b1_walk2], se=walk_se)
walk_choice_page = Page(walk_choice_img, [b1_walk_choice, b2_walk_choice])
hug_bear_page = Page(hug_bear_img, [b1_hug_bear])
hug_page = Page(hug_img, [b1_hug])
pet_dog_page = Page(pet_dog_img, [b1_pet_dog], se=panting_se)
pet_page = Page(pet_img, [b1_pet])
wed_page = Page(wed_img, [b1_wed])

knock_page = Page(knock_img, [b1_knock], se=knock_se)
birthday_page = Page(birthday_img, [b1_birthday], se=clap_se)
happy_page = Page(happy_img, [b1_happy])
thur_page = Page(thur_img, [b1_thur])

clean1_page = Page(clean1_img, [b1_clean1])
clean2_page = Page(clean2_img, [b1_clean2])
fri_page = Page(fri_img, [b1_fri])

walk3_page = Page(walk_img, [b1_walk3], se=walk_se)
shop_page = Page(shop_img, [b1_shop])
keeper1_page = Page(keeper1_img, [b1_keeper, b2_keeper, b3_keeper1])
keeper2_page = Page(keeper2_img, [b1_keeper, b2_keeper, b3_keeper2], se=partyhorn_se)
fire_page = Page(fire_img, [b1_fire])
sheep_page = Page(sheep_img, [b1_sheep])
sat_page = Page(sat_img, [b1_sat])

knock2_page = Page(knock2_img, [b1_knock2], se=knock_se)
ufo_page = Page(ufo_img, [b1_ufo])
obtain_ufo_page = Page(obtain_ufo_img, [b1_obtain_ufo])
sun_page = Page(sun_img, [b1_sun])
instruction_page = Page(instruction_img, [b1_instruction])

dead_page = Page(dead_img, [b1_dead])
game_over_page = Page(game_over_img, [b1_game_over])
run_page = Page(run_img, [b1_run])
save_page = Page(save_img, [b1_save])
celebrate_page = Page(celebrate_img, [b1_celebrate])
credit_page = Page(credit_img, [b1_credit])
thank_page = Page(thank_img, [b1_thank])

# set button target
b1_intro.target_page = walk_page
b1_walk.target_page = notice_page
b1_notice.target_page = poster_page
b1_poster.target_page = idea_page
b1_idea.target_page = tue_page

b1_tue.target_page = idle_day_page
b1_idle_day.target_page = routine_page
b1_routine.target_page = eat_page
b2_routine.target_page = workout_page
b1_eat.target_page = health_page
b1_workout.target_page = speed_page
b1_health.target_page = idle_night_page
b1_speed.target_page = idle_night_page

b1_idle_night.target_page = ev1_choice_page
b1_ev1_choice.target_page = go_out_page
b1_go_out.target_page = walk2_page
b2_go_out.target_page = walk2_page
b2_ev1_choice.target_page = walk2_page
b1_walk2.target_page = walk_choice_page
b1_walk_choice.target_page = hug_bear_page
b1_hug_bear.target_page = hug_page
b1_hug.target_page = wed_page
b2_walk_choice.target_page = pet_dog_page
b1_pet_dog.target_page = pet_page
b1_pet.target_page = wed_page

b1_wed.target_page = routine_page
b1_knock.target_page = birthday_page
b1_birthday.target_page = happy_page
b1_happy.target_page = thur_page

b1_thur.target_page = routine_page
b1_clean1.target_page = clean2_page
b1_clean2.target_page = fri_page

b1_fri.target_page = routine_page
b1_walk3.target_page = shop_page
b1_shop.target_page = keeper1_page
b1_keeper.target_page = fire_page
b2_keeper.target_page = sheep_page
b3_keeper1.target_page = keeper2_page
b3_keeper2.target_page = keeper1_page
b1_fire.target_page = sat_page
b1_sheep.target_page = sat_page

b1_sat.target_page = routine_page
b1_knock2.target_page = ufo_page
b1_ufo.target_page = obtain_ufo_page
b1_obtain_ufo.target_page = sun_page
b1_sun.target_page = instruction_page

b1_dead.target_page = game_over_page
b1_game_over.target_page = intro_page
b1_run.target_page = save_page
b1_save.target_page = celebrate_page
b1_celebrate.target_page = credit_page
b1_credit.target_page = thank_page
b1_thank.target_page = intro_page

# initialize game
day = 0
win = False
hero_speed = 3
hero_health = 5
bullet = 'fire_bullet'
current_page = 0
intro_page.make_current()
pygame.mixer.music.play(-1)

while True:

	current_page.show(screen)

	event_list = pygame.event.get()
	for event in event_list:

		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		if event.type == pygame.MOUSEBUTTONUP:
			(mouse_x, mouse_y) = event.pos
			for button in current_page.button_list:
				in_x = mouse_x >= button.region[0] and mouse_x <= button.region[2]
				in_y = mouse_y >= button.region[1] and mouse_y <= button.region[3]
				if in_x and in_y:
					if button == quit_button:
						pygame.quit()
						quit()

					# routine event
					elif button == b1_eat:
						day += 1
						hero_health += 1
						button.press()
					elif button == b1_workout:
						day += 1
						hero_speed += 1
						button.press()

					# special event
					elif button == b1_idle_night:
						if day == 1:
							ev1_choice_page.make_current()
						elif day == 2:
							knock_page.make_current()
						elif day == 3:
							clean1_page.make_current()
						elif day == 4:
							walk3_page.make_current()
						elif day == 5:
							knock2_page.make_current()
						current_page.show(screen)

					elif button == b2_keeper:
						bullet = 'sheep'
						button.press()

					# hell shooter button
					elif button == b1_instruction:
						hell_shooter(fps, screen, clock, bullet)
						if win is False:
							dead_page.make_current()
						else:
							run_page.make_current()
						day = 0
						bullet = 'fire_bullet'
						current_page.show(screen)

					else: 
						button.press()
					break

	(mouse_x, mouse_y) = pygame.mouse.get_pos()
	for button in current_page.button_list:
		in_x = (mouse_x >= button.region[0] and mouse_x <= button.region[2])
		in_y = (mouse_y >= button.region[1] and mouse_y <= button.region[3])
		if in_x and in_y:
			button.glow(screen)

	pygame.display.update()
	clock.tick(fps)
