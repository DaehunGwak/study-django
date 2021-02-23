# model test project

브랜치, 커밋 레벨이 아닌 코드 레벨에서 모델 정의를 분리할 수 있을까에 대한 고민 프로젝트

> 실제 프로젝트에선 각 환경별 디비 스킴이 동일하도록 구성되는게 베스트 프랙티스라 생각한다.
> 하지만 세상의 모든일이 그렇듯 베스트 프랙티스를 따라가지 못하는 상황은 생겨나기 마련이고,
> 이를 대비하는 안티 패턴을 알아두고 필요 시 사용하는 자세도 필요하다 생각된다. (개인적인 의견)

## 얻고자 하는것

- 코드 레벨의 환경 별 모델 정의 분리

## environments

- python 3.9.1
- django 3.1
- django rest framework 3.12

## 해결방안 

### 1. settings 변수로 model 클래스내 필드구성을 분기

> 클래스의 인스턴스 변수를 if 로 분기하는 것이 조금 이상해 보인다 (어짜피 안티 패턴이라 상관 없는 것인가..)

```python
class DummyTable(models.Model):
    if settings.ENV_NAME == 'env_local':
        local_field = models.IntegerField('로컬 필드', default=0, blank=True)
    else:
        production_field = models.IntegerField("프로덕션 필드", default=1, blank=False)
```

## 추가적으로

### DJANGO_SETTINGS_MODULE export

production 레벨의 db 마이그레이션이 필요할 땐 export 후 사용

> OS에 (.bashrc, .zshrc 등) 미리 등록해서 사용해두면 환경 구성 시 편함

```shell
# production 마이그레이션 필요 시
export DJANGO_SETTINGS_MODULE=modeltest.settings.production

# local 마이그레이션 사용으로 초기화 하고 싶을 시
export DJANGO_SETTINGS_MODULE=modeltest.settings.local
```
