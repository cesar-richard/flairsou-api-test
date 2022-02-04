import React, { useEffect, useState } from 'react';
import ContentWrapper from '../../UI/organisms/ContentWrapper/ContentWrapper';
import HomeContent from '../../UI/organisms/HomeContent/HomeContent';

const Home = () => {
  const [authLink, setAuthLink] = useState('');
  const [userName, setUserName] = useState('NOT_FETCHED');

  const authlinkUrl = '/oauth/authlink';
  const userInfosUrl = '/proxy_pda/get_user_infos';

  useEffect(() => {
    fetch(authlinkUrl)
      .then((response) => response.json())
      .then((response) => {
        setAuthLink(response.link);
      });
  }, []);

  useEffect(() => {
    fetch(userInfosUrl)
      .then((response) => {
        if (response.status === 200) {
          response.json().then((validResponse) => {
            const fullName = `${validResponse.firstname} ${validResponse.lastname}`;
            setUserName(fullName);
          });
        } else {
          setUserName('');
        }
      });
  }, []);

  useEffect(() => {
    console.log(`userName: ${userName}; authLink: ${authLink};`);
    if (userName === '' && authLink !== '') {
      console.log('redirecting...');
      window.location.href = authLink;
    }
  }, [userName, authLink]);

  return (
    <ContentWrapper content={<HomeContent />} />
  );
};

export default Home;
