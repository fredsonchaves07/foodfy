// TODO -> refatorar todo os scripts
const modal = document.querySelector('.modal-background')
const receitas = document.querySelectorAll('.receitas')

const currentPage = location.pathname
const menuItem = document.querySelectorAll('header div:nth-child(2) a')

for(item of menuItem){
    if(currentPage.includes(item.getAttribute('href'))){
        item.classList.add('active')
    }
}

for(let receita of receitas){
    receita.addEventListener("click", function(){
        modal.classList.add('active')
        var endereco_imagem = receita.querySelector('img').src
        var nome_imagem = receita.querySelector('img').alt
        var info_receita = receita.querySelector('.info').textContent
        var autor = receita.querySelector('.autor').textContent
        modal.querySelector('img').src = endereco_imagem
        modal.querySelector('img').alt = nome_imagem
        modal.querySelector('.info').textContent = info_receita
        modal.querySelector('.autor').textContent = autor
    })
}

const PhotosUpload = {
    uploadLimit: 5,
    photosList: [],
    photoPreview: document.querySelector('#photos-preview'),
    inputFile: '',
    photoRemoveId: [],

    fileUpload(event){
        const {files: fileList} = event.target
        PhotosUpload.inputFile = event.target


        if(PhotosUpload.hasLimit(event)){
            return
        }

        Array.from(fileList).forEach(file => {
            PhotosUpload.photosList.push(file)

            const reader = new FileReader()

            reader.onload = () => {
                const image = new Image()
                image.src = String(reader.result)

                const div = PhotosUpload.getDivContainter(image)

                PhotosUpload.photoPreview.appendChild(div)
            }

            reader.readAsDataURL(file)
        })

        PhotosUpload.inputFile.files = PhotosUpload.getAllFiles()
    },

    getAllFiles(){
        const dataTransfer = new DataTransfer || new ClipboardEvent('')

        PhotosUpload.photosList.forEach(file => dataTransfer.items.add(file))

        return dataTransfer.files
    },

    hasLimit(event){
        const {uploadLimit, inputFile, photoPreview} = PhotosUpload
        const {files: fileList} = inputFile
        
        if(fileList.length > uploadLimit){
            alert(`Envie no máximo ${uploadLimit} fotos`)
            event.preventDefault()
            return true
        }

        const photoDiv = []

        photoPreview.childNodes.forEach(item => {
            if(item.classList && item.classList.value == 'photo'){
                photoDiv.push(item)
            }
        })

        const totalPhotos = fileList.length + photoDiv.length

        if(totalPhotos > uploadLimit){
            alert('Atingiu o limite de fotos')
            event.preventDefault()
            return true
        }

        return false
    },

    getDivContainter(image){
        const div = document.createElement('div')

        div.classList.add('photo')
        div.onclick = PhotosUpload.removePhoto
        div.appendChild(PhotosUpload.getRemoveButton())
        div.appendChild(image)

        return div
    },

    getRemoveButton(){
        const button = document.createElement('i')
        button.classList.add('material-icons')
        button.innerHTML = 'close'

        return button
    },

    removePhoto(event){
        const photoDiv = event.target.parentNode
        const photoId = photoDiv.children[0].id
        const photoArray = Array.from(PhotosUpload.photoPreview.children)
        const index = photoArray.indexOf(photoDiv)
       
        if(photoId){
            const removedFiles = document.querySelector('input[name="removed_files"]')

            if(removedFiles){
                PhotosUpload.photoRemoveId.push(photoId)
            }

            removedFiles.value = PhotosUpload.photoRemoveId
        }

        PhotosUpload.photosList.splice(index - 3, 1)
        PhotosUpload.inputFile.files = PhotosUpload.getAllFiles()
        photoDiv.remove()

    },

}

const ImageGallery = {
    imgHeader: document.querySelector('.recipe-show-header > img'),
    galleryPreview: document.querySelectorAll('.recipe-gallery > img'),
    setImage(event){
        const {target} = event
        imgPreview = target

        ImageGallery.galleryPreview.forEach(image => {
            image.classList.remove('active')
        })

        imgPreview.classList.add('active')

        ImageGallery.imgHeader.src = imgPreview.src
    }
}

const PhotoChef = {
    img: document.querySelector('.content-form-avatar img'),

    change(event){
        const {files} = event.target

        Array.from(files).forEach(file => {
            const reader = new FileReader()

            reader.onload = () => {
                const image = new Image()
                image.src = String(reader.result)
                PhotoChef.img.src = image.src
            }
    
            reader.readAsDataURL(file)
        })
    }
}
