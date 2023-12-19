import styles from "./SetAddressScreen.module.css";

const SetAddressScreen = () => {
    return (
        <div className={styles.setaddressscreen}>
            <div className={styles.filters}>
                <div className={styles.action}>
                    <div className={styles.buttonPrimary}>
                        <div className={styles.leftIcon}>
                            <div className={styles.fill} />
                        </div>
                        <div className={styles.button}>주소 저장</div>
                        <div className={styles.rightIcon}>
                            <div className={styles.fill} />
                        </div>
                    </div>
                </div>
                <div className={styles.filters1}>
                    <div className={styles.search}>
                        <div className={styles.fill2} />
                    </div>
                    <div className={styles.listItem}>
                        <div className={styles.content}>
                            <div className={styles.title}>도로명으로 검색</div>
                            <div className={styles.description}>xxxx xxxx xxxx 9876</div>
                        </div>
                        <div className={styles.badge}>
                            <div className={styles.div}>1</div>
                        </div>
                    </div>
                    <img className={styles.dividerIcon} alt="" src="/divider.svg" />
                    <div className={styles.listItem}>
                        <div className={styles.content}>
                            <div className={styles.title}>상세주소</div>
                            <div className={styles.description}>xxxx xxxx xxxx 9876</div>
                        </div>
                        <div className={styles.rightButton}>
                            <div className={styles.fill3} />
                        </div>
                    </div>
                    <img className={styles.dividerIcon} alt="" src="/divider.svg" />
                    <img className={styles.dividerIcon2} alt="" src="/divider1.svg" />
                </div>
                {/* <div className={styles.navBar}>
                    <div className={styles.pageTitle}>주소 설정</div>
                    <div className={styles.rightButton1}>Home</div>
                    <div className={styles.rightButton2}>Clear All</div>
                </div> */}
            </div>
        </div>
    );
};

export default SetAddressScreen;