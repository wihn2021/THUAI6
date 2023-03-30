from math import pi
from concurrent.futures import ThreadPoolExecutor, Future
from typing import List, cast
import logging
import os
import datetime

import PyAPI.structures as THUAI6
from PyAPI.Interface import ILogic, IStudentAPI, ITrickerAPI, IGameTimer, IAI


class StudentDebugAPI(IStudentAPI, IGameTimer):

    def __init__(self, logic: ILogic, file: bool, screen: bool, warnOnly: bool, playerID: int) -> None:
        self.__logic = logic
        self.__pool = ThreadPoolExecutor(20)
        self.__startPoint = datetime.datetime.now()
        self.__logger = logging.getLogger("api " + str(playerID))
        self.__logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "[%(name)s] [%(asctime)s] [%(levelname)s] %(message)s", "%H:%M:%S.%e")
        # 确保文件存在
        if not os.path.exists(os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/logs"):
            os.makedirs(os.path.dirname(os.path.dirname(
                os.path.realpath(__file__))) + "/logs")

        fileHandler = logging.FileHandler(os.path.dirname(
            os.path.dirname(os.path.realpath(__file__))) + "/logs/api-" + str(playerID) + "-log.txt", mode="w+", encoding="utf-8")
        screenHandler = logging.StreamHandler()
        if file:
            fileHandler.setLevel(logging.DEBUG)
            fileHandler.setFormatter(formatter)
            self.__logger.addHandler(fileHandler)
        if screen:
            if warnOnly:
                screenHandler.setLevel(logging.WARNING)
            else:
                screenHandler.setLevel(logging.INFO)
            screenHandler.setFormatter(formatter)
            self.__logger.addHandler(screenHandler)

    # 指挥本角色进行移动，`timeInMilliseconds` 为移动时间，单位为毫秒；`angleInRadian` 表示移动的方向，单位是弧度，使用极坐标——竖直向下方向为 x 轴，水平向右方向为 y 轴

    def Move(self, timeInMilliseconds: int, angle: float) -> Future[bool]:
        self.__logger.info(
            f"Move: timeInMilliseconds = {timeInMilliseconds}, angle = {angle}, called at {self.__GetTime()}ms")

        def logMove() -> bool:
            result = self.__logic.Move(timeInMilliseconds, angle)
            if not result:
                self.__logger.warning(
                    f"Move: failed at {self.__GetTime()}ms")
            return result

        return self.__pool.submit(logMove)

    # 向特定方向移动

    def MoveRight(self, timeInMilliseconds: int) -> Future[bool]:
        return self.Move(timeInMilliseconds, pi * 0.5)

    def MoveLeft(self, timeInMilliseconds: int) -> Future[bool]:
        return self.Move(timeInMilliseconds, pi * 1.5)

    def MoveUp(self, timeInMilliseconds: int) -> Future[bool]:
        return self.Move(timeInMilliseconds, pi)

    def MoveDown(self, timeInMilliseconds: int) -> Future[bool]:
        return self.Move(timeInMilliseconds, 0)

    def Attack(self, angle: float) -> Future[bool]:
        self.__logger.info(
            f"Attack: angle = {angle}, called at {self.__GetTime()}ms")

        def logAttack() -> bool:
            result = self.__logic.Attack(angle)
            if not result:
                self.__logger.warning(
                    f"Attack: failed at {self.__GetTime()}ms")
            return result

        return self.__pool.submit(logAttack)

    # 道具和技能相关

    def PickProp(self, propType: THUAI6.PropType) -> Future[bool]:
        self.__logger.info(
            f"PickProp: prop = {propType.name}, called at {self.__GetTime()}ms")

        def logPick() -> bool:
            result = self.__logic.PickProp(propType)
            if not result:
                self.__logger.warning(
                    f"PickProp: failed at {self.__GetTime()}ms")
            return result

        return self.__pool.submit(logPick)

    def UseProp(self, propType: THUAI6.PropType) -> Future[bool]:
        self.__logger.info(
            f"UseProp: prop = {propType.name}, called at {self.__GetTime()}ms")

        def logUse() -> bool:
            result = self.__logic.UseProp(propType)
            if not result:
                self.__logger.warning(
                    f"UseProp: failed at {self.__GetTime()}ms")
            return result

        return self.__pool.submit(logUse)

    def UseSkill(self, skillID: int) -> Future[bool]:
        self.__logger.info(
            f"UseSkill: skillID = {skillID}, called at {self.__GetTime()}ms")

        def logUse() -> bool:
            result = self.__logic.UseSkill(skillID)
            if not result:
                self.__logger.warning(
                    f"UseSkill: failed at {self.__GetTime()}ms")
            return result

        return self.__pool.submit(logUse)

    # 与地图交互相关
    def OpenDoor(self) -> Future[bool]:
        self.__logger.info(
            f"OpenDoor: called at {self.__GetTime()}ms")

        def logOpen() -> bool:
            result = self.__logic.OpenDoor()
            if not result:
                self.__logger.warning(
                    f"OpenDoor: failed at {self.__GetTime()}ms")
            return result

        return self.__pool.submit(logOpen)

    def CloseDoor(self) -> Future[bool]:
        self.__logger.info(
            f"CloseDoor: called at {self.__GetTime()}ms")

        def logClose() -> bool:
            result = self.__logic.CloseDoor()
            if not result:
                self.__logger.warning(
                    f"CloseDoor: failed at {self.__GetTime()}ms")
            return result

        return self.__pool.submit(logClose)

    def SkipWindow(self) -> Future[bool]:
        self.__logger.info(
            f"SkipWindow: called at {self.__GetTime()}ms")

        def logSkip() -> bool:
            result = self.__logic.SkipWindow()
            if not result:
                self.__logger.warning(
                    f"SkipWindow: failed at {self.__GetTime()}ms")
            return result

        return self.__pool.submit(logSkip)

    def StartOpenGate(self) -> Future[bool]:
        self.__logger.info(
            f"StartOpenGate: called at {self.__GetTime()}ms")

        def logStart() -> bool:
            result = self.__logic.StartOpenGate()
            if not result:
                self.__logger.warning(
                    f"StartOpenGate: failed at {self.__GetTime()}ms")
            return result

        return self.__pool.submit(logStart)

    def StartOpenChest(self) -> Future[bool]:
        self.__logger.info(
            f"StartOpenChest: called at {self.__GetTime()}ms")

        def logStart() -> bool:
            result = self.__logic.StartOpenChest()
            if not result:
                self.__logger.warning(
                    f"StartOpenChest: failed at {self.__GetTime()}ms")
            return result

        return self.__pool.submit(logStart)

    def EndAllAction(self) -> Future[bool]:
        self.__logger.info(
            f"EndAllAction: called at {self.__GetTime()}ms")

        def logEnd() -> bool:
            result = self.__logic.EndAllAction()
            if not result:
                self.__logger.warning(
                    f"EndAllAction: failed at {self.__GetTime()}ms")
            return result

        return self.__pool.submit(logEnd)

    # 消息相关，接收消息时无消息则返回(-1, '')

    def SendMessage(self, toID: int, message: str) -> Future[bool]:
        self.__logger.info(
            f"SendMessage: toID = {toID}, message = {message}, called at {self.__GetTime()}ms")

        def logSend() -> bool:
            result = self.__logic.SendMessage(toID, message)
            if not result:
                self.__logger.warning(
                    f"SendMessage: failed at {self.__GetTime()}ms")
            return result

        return self.__pool.submit(logSend)

    def HaveMessage(self) -> bool:
        self.__logger.info(
            f"HaveMessage: called at {self.__GetTime()}ms")
        result = self.__logic.HaveMessage()
        if not result:
            self.__logger.warning(
                f"HaveMessage: failed at {self.__GetTime()}ms")
        return result

    def GetMessage(self) -> tuple[int, str]:
        self.__logger.info(
            f"GetMessage: called at {self.__GetTime()}ms")
        result = self.__logic.GetMessage()
        if result[0] == -1:
            self.__logger.warning(
                f"GetMessage: failed at {self.__GetTime()}ms")
        return result

    # 等待下一帧

    def Wait(self) -> Future[bool]:
        self.__logger.info(
            f"Wait: called at {self.__GetTime()}ms")
        if self.__logic.GetCounter() == -1:
            return self.__pool.submit(lambda: False)
        else:
            return self.__pool.submit(self.__logic.WaitThread)

    # 获取各类游戏中的消息

    def GetFrameCount(self) -> int:
        return self.__logic.GetCounter()

    def GetPlayerGUIDs(self) -> List[int]:
        return self.__logic.GetPlayerGUIDs()

    def GetTrickers(self) -> List[THUAI6.Tricker]:
        return self.__logic.GetTrickers()

    def GetStudents(self) -> List[THUAI6.Student]:
        return self.__logic.GetStudents()

    def GetProps(self) -> List[THUAI6.Prop]:
        return self.__logic.GetProps()

    def GetFullMap(self) -> List[List[THUAI6.PlaceType]]:
        return self.__logic.GetFullMap()

    def GetPlaceType(self, cellX: int, cellY: int) -> THUAI6.PlaceType:
        return self.__logic.GetPlaceType(cellX, cellY)

    def IsDoorOpen(self, cellX: int, cellY: int) -> bool:
        return self.__logic.IsDoorOpen(cellX, cellY)

    def GetChestProgress(self, cellX: int, cellY: int) -> int:
        return self.__logic.GetChestProgress(cellX, cellY)

    def GetGateProgress(self, cellX: int, cellY: int) -> int:
        return self.__logic.GetGateProgress(cellX, cellY)

    def GetClassroomProgress(self, cellX: int, cellY: int) -> int:
        return self.__logic.GetClassroomProgress(cellX, cellY)

    def GetDoorProgress(self, cellX: int, cellY: int) -> int:
        return self.__logic.GetDoorProgress(cellX, cellY)

    def GetHiddenGateState(self, cellX: int, cellY: int) -> THUAI6.HiddenGateState:
        return self.__logic.GetHiddenGateState(cellX, cellY)

    def GetGameInfo(self) -> THUAI6.GameInfo:
        return self.__logic.GetGameInfo()

    # 用于DEBUG的输出函数，仅在DEBUG模式下有效

    def Print(self, cont: str) -> None:
        self.__logger.info(cont)

    def PrintStudent(self) -> None:
        for student in self.__logic.GetStudents():
            self.__logger.info("******Student Info******")
            self.__logger.info(
                f"playerID={student.playerID}, GUID={student.guid}, x={student.x}, y={student.y}")
            self.__logger.info(
                f"speed={student.speed}, view range={student.viewRange}, skill time={student.timeUntilSkillAvailable},place={student.place.name}")
            studentBuff = "buff="
            for buff in student.buff:
                studentBuff += buff.name + ", "
            self.__logger.info(studentBuff)
            studentProp = "prop="
            for prop in student.prop:
                studentProp += prop.name + ", "
            self.__logger.info(studentProp)
            self.__logger.info("**********************")

    def PrintTricker(self) -> None:
        for tricker in self.__logic.GetTrickers():
            self.__logger.info("******Tricker Info******")
            self.__logger.info(
                f"playerID={tricker.playerID}, GUID={tricker.guid}, x={tricker.x}, y={tricker.y}")
            self.__logger.info(
                f"speed={tricker.speed}, view range={tricker.viewRange}, skill time={tricker.timeUntilSkillAvailable},  place={tricker.place.name}")
            self.__logger.info("buff=")
            trickerBuff = ""
            for buff in tricker.buff:
                trickerBuff += buff.name + ", "
            self.__logger.info(trickerBuff)
            self.__logger.info("************************")

    def PrintProp(self) -> None:
        for prop in self.__logic.GetProps():
            self.__logger.info("******Prop Info******")
            self.__logger.info(
                f"GUID={prop.guid}, x={prop.x}, y={prop.y}, place={prop.place.name}, ")
            self.__logger.info("*********************")

    def PrintSelfInfo(self) -> None:
        mySelf = self.__logic.GetSelfInfo()
        self.__logger.info("******Self Info******")
        self.__logger.info(
            f"playerID={mySelf.playerID}, GUID={mySelf.guid}, x={mySelf.x}, y={mySelf.y}")
        self.__logger.info(
            f"speed={mySelf.speed}, view range={mySelf.viewRange}, skill time={mySelf.timeUntilSkillAvailable}, place={mySelf.place.name}")
        if isinstance(mySelf, THUAI6.Student):
            self.__logger.info(
                f"state={mySelf.playerState.name}, determination={mySelf.determination},")
        mySelfBuff = "buff="
        for buff in mySelf.buff:
            mySelfBuff += buff.name + ", "
        self.__logger.info(mySelfBuff)
        studentProp = "prop="
        for prop in mySelf.prop:
            studentProp += prop.name + ", "
        self.__logger.info(studentProp)
        self.__logger.info("*********************")

    # 人类阵营的特殊函数

    def Graduate(self) -> Future[bool]:
        self.__logger.info(
            f"Graduate: called at {self.__GetTime()}ms")

        def logGraduate() -> bool:
            result = self.__logic.Graduate()
            if not result:
                self.__logger.warning(
                    f"Graduate: failed at {self.__GetTime()}ms")
            return result

        return self.__pool.submit(logGraduate)

    def StartLearning(self) -> Future[bool]:
        self.__logger.info(
            f"StartLearning: called at {self.__GetTime()}ms")

        def logStart() -> bool:
            result = self.__logic.StartLearning()
            if not result:
                self.__logger.warning(
                    f"StartLearning: failed at {self.__GetTime()}ms")
            return result

        return self.__pool.submit(logStart)

    def StartTreatMate(self, mateID: int) -> Future[bool]:
        self.__logger.info(
            f"StartTreatMate: called at {self.__GetTime()}ms")

        def logStartTreatMate() -> bool:
            result = self.__logic.StartTreatMate(mateID)
            if not result:
                self.__logger.warning(
                    f"StartTreatMate: failed at {self.__GetTime()}ms")
            return result

        return self.__pool.submit(logStartTreatMate)

    def StartRescueMate(self, mateID: int) -> Future[bool]:
        self.__logger.info(
            f"StartRescueMate: called at {self.__GetTime()}ms")

        def logStartRescueMate() -> bool:
            result = self.__logic.StartRescueMate(mateID)
            if not result:
                self.__logger.warning(
                    f"StartRescueMate: failed at {self.__GetTime()}ms")
            return result

        return self.__pool.submit(logStartRescueMate)

    def GetSelfInfo(self) -> THUAI6.Student:
        return cast(THUAI6.Student, self.__logic.GetSelfInfo())

    # Timer用

    def __GetTime(self) -> int:
        return int((datetime.datetime.now() - self.__startPoint).total_seconds() * 1000)

    def StartTimer(self) -> None:
        self.__startPoint = datetime.datetime.now()
        self.__logger.info("=== AI.play() ===")
        self.__logger.info(f"StartTimer: {self.__startPoint.time()}")

    def EndTimer(self) -> None:
        self.__logger.info(f"Time elapsed: {self.__GetTime()}ms")

    def Play(self, ai: IAI) -> None:
        ai.StudentPlay(self)


class TrickerDebugAPI(ITrickerAPI, IGameTimer):

    def __init__(self, logic: ILogic, file: bool, screen: bool, warnOnly: bool, playerID: int) -> None:
        self.__logic = logic
        self.__pool = ThreadPoolExecutor(20)
        self.__logger = logging.getLogger("api " + str(playerID))
        self.__logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "[%(name)s] [%(asctime)s] [%(levelname)s] %(message)s", "%H:%M:%S.%e")
        # 确保文件存在
        if not os.path.exists(os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/logs"):
            os.makedirs(os.path.dirname(os.path.dirname(
                os.path.realpath(__file__))) + "/logs")

        fileHandler = logging.FileHandler(os.path.dirname(
            os.path.dirname(os.path.realpath(__file__))) + "/logs/api-" + str(playerID) + "-log.txt", mode="w+", encoding="utf-8")
        screenHandler = logging.StreamHandler()
        if file:
            fileHandler.setLevel(logging.DEBUG)
            fileHandler.setFormatter(formatter)
            self.__logger.addHandler(fileHandler)
        if screen:
            if warnOnly:
                screenHandler.setLevel(logging.WARNING)
            else:
                screenHandler.setLevel(logging.INFO)
            screenHandler.setFormatter(formatter)
            self.__logger.addHandler(screenHandler)

    # 指挥本角色进行移动，`timeInMilliseconds` 为移动时间，单位为毫秒；`angleInRadian` 表示移动的方向，单位是弧度，使用极坐标——竖直向下方向为 x 轴，水平向右方向为 y 轴

    def Move(self, timeInMilliseconds: int, angle: float) -> Future[bool]:
        self.__logger.info(
            f"Move: timeInMilliseconds = {timeInMilliseconds}, angle = {angle}, called at {self.__GetTime()}ms")

        def logMove() -> bool:
            result = self.__logic.Move(timeInMilliseconds, angle)
            if not result:
                self.__logger.warning(
                    f"Move: failed at {self.__GetTime()}ms")
            return result

        return self.__pool.submit(logMove)

    # 向特定方向移动

    def MoveRight(self, timeInMilliseconds: int) -> Future[bool]:
        return self.Move(timeInMilliseconds, pi * 0.5)

    def MoveLeft(self, timeInMilliseconds: int) -> Future[bool]:
        return self.Move(timeInMilliseconds, pi * 1.5)

    def MoveUp(self, timeInMilliseconds: int) -> Future[bool]:
        return self.Move(timeInMilliseconds, pi)

    def MoveDown(self, timeInMilliseconds: int) -> Future[bool]:
        return self.Move(timeInMilliseconds, 0)

    # 道具和技能相关

    def Attack(self, angle: float) -> Future[bool]:
        self.__logger.info(
            f"Attack: angle = {angle}, called at {self.__GetTime()}ms")

        def logAttack() -> bool:
            result = self.__logic.Attack(angle)
            if not result:
                self.__logger.warning(
                    f"Attack: failed at {self.__GetTime()}ms")
            return result

        return self.__pool.submit(logAttack)

    # 道具和技能相关

    def PickProp(self, propType: THUAI6.PropType) -> Future[bool]:
        self.__logger.info(
            f"PickProp: prop = {propType.name}, called at {self.__GetTime()}ms")

        def logPick() -> bool:
            result = self.__logic.PickProp(propType)
            if not result:
                self.__logger.warning(
                    f"PickProp: failed at {self.__GetTime()}ms")
            return result

        return self.__pool.submit(logPick)

    def UseProp(self, propType: THUAI6.PropType) -> Future[bool]:
        self.__logger.info(
            f"UseProp: prop = {propType.name}, called at {self.__GetTime()}ms")

        def logUse() -> bool:
            result = self.__logic.UseProp(propType)
            if not result:
                self.__logger.warning(
                    f"UseProp: failed at {self.__GetTime()}ms")
            return result

        return self.__pool.submit(logUse)

    def UseSkill(self, skillID: int) -> Future[bool]:
        self.__logger.info(
            f"UseSkill: skillID = {skillID}, called at {self.__GetTime()}ms")

        def logUse() -> bool:
            result = self.__logic.UseSkill(skillID)
            if not result:
                self.__logger.warning(
                    f"UseSkill: failed at {self.__GetTime()}ms")
            return result

        return self.__pool.submit(logUse)

    # 与地图交互相关
    def OpenDoor(self) -> Future[bool]:
        self.__logger.info(
            f"OpenDoor: called at {self.__GetTime()}ms")

        def logOpen() -> bool:
            result = self.__logic.OpenDoor()
            if not result:
                self.__logger.warning(
                    f"OpenDoor: failed at {self.__GetTime()}ms")
            return result

        return self.__pool.submit(logOpen)

    def CloseDoor(self) -> Future[bool]:
        self.__logger.info(
            f"CloseDoor: called at {self.__GetTime()}ms")

        def logClose() -> bool:
            result = self.__logic.CloseDoor()
            if not result:
                self.__logger.warning(
                    f"CloseDoor: failed at {self.__GetTime()}ms")
            return result

        return self.__pool.submit(logClose)

    def SkipWindow(self) -> Future[bool]:
        self.__logger.info(
            f"SkipWindow: called at {self.__GetTime()}ms")

        def logSkip() -> bool:
            result = self.__logic.SkipWindow()
            if not result:
                self.__logger.warning(
                    f"SkipWindow: failed at {self.__GetTime()}ms")
            return result

        return self.__pool.submit(logSkip)

    def StartOpenGate(self) -> Future[bool]:
        self.__logger.info(
            f"StartOpenGate: called at {self.__GetTime()}ms")

        def logStart() -> bool:
            result = self.__logic.StartOpenGate()
            if not result:
                self.__logger.warning(
                    f"StartOpenGate: failed at {self.__GetTime()}ms")
            return result

        return self.__pool.submit(logStart)

    def StartOpenChest(self) -> Future[bool]:
        self.__logger.info(
            f"StartOpenChest: called at {self.__GetTime()}ms")

        def logStart() -> bool:
            result = self.__logic.StartOpenChest()
            if not result:
                self.__logger.warning(
                    f"StartOpenChest: failed at {self.__GetTime()}ms")
            return result

        return self.__pool.submit(logStart)

    def EndAllAction(self) -> Future[bool]:
        self.__logger.info(
            f"EndAllAction: called at {self.__GetTime()}ms")

        def logEnd() -> bool:
            result = self.__logic.EndAllAction()
            if not result:
                self.__logger.warning(
                    f"EndAllAction: failed at {self.__GetTime()}ms")
            return result

        return self.__pool.submit(logEnd)

    # 消息相关，接收消息时无消息则返回(-1, '')

    def SendMessage(self, toID: int, message: str) -> Future[bool]:
        self.__logger.info(
            f"SendMessage: toID = {toID}, message = {message}, called at {self.__GetTime()}ms")

        def logSend() -> bool:
            result = self.__logic.SendMessage(toID, message)
            if not result:
                self.__logger.warning(
                    f"SendMessage: failed at {self.__GetTime()}ms")
            return result

        return self.__pool.submit(logSend)

    def HaveMessage(self) -> bool:
        self.__logger.info(
            f"HaveMessage: called at {self.__GetTime()}ms")
        result = self.__logic.HaveMessage()
        if not result:
            self.__logger.warning(
                f"HaveMessage: failed at {self.__GetTime()}ms")
        return result

    def GetMessage(self) -> tuple[int, str]:
        self.__logger.info(
            f"GetMessage: called at {self.__GetTime()}ms")
        result = self.__logic.GetMessage()
        if result[0] == -1:
            self.__logger.warning(
                f"GetMessage: failed at {self.__GetTime()}ms")
        return result

    # 等待下一帧

    def Wait(self) -> Future[bool]:
        self.__logger.info(
            f"Wait: called at {self.__GetTime()}ms")
        if self.__logic.GetCounter() == -1:
            return self.__pool.submit(lambda: False)
        else:
            return self.__pool.submit(self.__logic.WaitThread)

    # 获取各类游戏中的消息

    def GetFrameCount(self) -> int:
        return self.__logic.GetCounter()

    def GetPlayerGUIDs(self) -> List[int]:
        return self.__logic.GetPlayerGUIDs()

    def GetTrickers(self) -> List[THUAI6.Tricker]:
        return self.__logic.GetTrickers()

    def GetStudents(self) -> List[THUAI6.Student]:
        return self.__logic.GetStudents()

    def GetProps(self) -> List[THUAI6.Prop]:
        return self.__logic.GetProps()

    def GetFullMap(self) -> List[List[THUAI6.PlaceType]]:
        return self.__logic.GetFullMap()

    def GetPlaceType(self, cellX: int, cellY: int) -> THUAI6.PlaceType:
        return self.__logic.GetPlaceType(cellX, cellY)

    def IsDoorOpen(self, cellX: int, cellY: int) -> bool:
        return self.__logic.IsDoorOpen(cellX, cellY)

    def GetChestProgress(self, cellX: int, cellY: int) -> int:
        return self.__logic.GetChestProgress(cellX, cellY)

    def GetGateProgress(self, cellX: int, cellY: int) -> int:
        return self.__logic.GetGateProgress(cellX, cellY)

    def GetClassroomProgress(self, cellX: int, cellY: int) -> int:
        return self.__logic.GetClassroomProgress(cellX, cellY)

    def GetDoorProgress(self, cellX: int, cellY: int) -> int:
        return self.__logic.GetDoorProgress(cellX, cellY)

    def GetHiddenGateState(self, cellX: int, cellY: int) -> THUAI6.HiddenGateState:
        return self.__logic.GetHiddenGateState(cellX, cellY)

    def GetGameInfo(self) -> THUAI6.GameInfo:
        return self.__logic.GetGameInfo()

    # 用于DEBUG的输出函数，仅在DEBUG模式下有效

    def Print(self, cont: str) -> None:
        self.__logger.info(cont)

    def PrintStudent(self) -> None:
        for student in self.__logic.GetStudents():
            self.__logger.info("******Student Info******")
            self.__logger.info(
                f"playerID={student.playerID}, GUID={student.guid}, x={student.x}, y={student.y}")
            self.__logger.info(
                f"speed={student.speed}, view range={student.viewRange}, skill time={student.timeUntilSkillAvailable}, place={student.place.name}")
            self.__logger.info(
                f"state={student.playerState.name}, determination={student.determination}")
            self.__logger.info("buff=")
            studentBuff = ""
            for buff in student.buff:
                studentBuff += buff.name + ", "
            self.__logger.info(studentBuff)
            self.__logger.info("**********************")

    def PrintTricker(self) -> None:
        for tricker in self.__logic.GetTrickers():
            self.__logger.info("******Tricker Info******")
            self.__logger.info(
                f"playerID={tricker.playerID}, GUID={tricker.guid}, x={tricker.x}, y={tricker.y}")
            self.__logger.info(
                f"speed={tricker.speed}, view range={tricker.viewRange}, skill time={tricker.timeUntilSkillAvailable}, place={tricker.place.name}")
            self.__logger.info("buff=")
            trickerBuff = ""
            for buff in tricker.buff:
                trickerBuff += buff.name + ", "
            self.__logger.info(trickerBuff)
            self.__logger.info("************************")

    def PrintProp(self) -> None:
        for prop in self.__logic.GetProps():
            self.__logger.info("******Prop Info******")
            self.__logger.info(
                f"GUID={prop.guid}, x={prop.x}, y={prop.y}, place={prop.place.name}")
            self.__logger.info("*********************")

    def PrintSelfInfo(self) -> None:
        mySelf = self.__logic.GetSelfInfo()
        self.__logger.info("******Self Info******")
        self.__logger.info(
            f"playerID={mySelf.playerID}, GUID={mySelf.guid}, x={mySelf.x}, y={mySelf.y}")
        self.__logger.info(
            f"speed={mySelf.speed}, view range={mySelf.viewRange}, skill time={mySelf.timeUntilSkillAvailable}, place={mySelf.place.name}")
        if isinstance(mySelf, THUAI6.Student):
            self.__logger.info(
                f"state={mySelf.playerState.name}, determination={mySelf.determination}")
        self.__logger.info("buff=")
        mySelfBuff = ""
        for buff in mySelf.buff:
            mySelfBuff += buff.name + ", "
        self.__logger.info(mySelfBuff)
        self.__logger.info("*********************")

    # 屠夫阵营的特殊函数

    def GetSelfInfo(self) -> THUAI6.Tricker:
        return cast(THUAI6.Tricker, self.__logic.GetSelfInfo())

    # Timer用

    def __GetTime(self) -> float:
        return (datetime.datetime.now() - self.__startPoint).total_seconds() * 1000

    def StartTimer(self) -> None:
        self.__startPoint = datetime.datetime.now()
        self.__logger.info("=== AI.play() ===")
        self.__logger.info(f"StartTimer: {self.__startPoint.time()}")

    def EndTimer(self) -> None:
        self.__logger.info(f"Time elapsed: {self.__GetTime()}ms")

    def Play(self, ai: IAI) -> None:
        ai.TrickerPlay(self)
