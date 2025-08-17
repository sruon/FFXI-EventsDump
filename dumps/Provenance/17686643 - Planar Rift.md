# 17686643 - Planar Rift

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Provenance (ID: 222) |
| Block Size       | 944 bytes            |
| Total Events     | 3                    |
| References Count | 19                   |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [15](#event-15)       | 0x0001       |     97 |             25 |
| [23](#event-23)       | 0x0062       |    742 |             81 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1E04      |        7684 |
|       1 | 0x1E05      |        7685 |
|       2 | 0x0000      |           0 |
|       3 | 0x00FF      |         255 |
|       4 | 0x004F      |          79 |
|       5 | 0x0096      |         150 |
|       6 | 0x0028      |          40 |
|       7 | 0x001E      |          30 |
|       8 | 0x0001      |           1 |
|       9 | 0x40000000  |  1073741824 |
|      10 | 0x1E06      |        7686 |
|      11 | 0x1CB6      |        7350 |
|      12 | 0x1CB7      |        7351 |
|      13 | 0x000A      |          10 |
|      14 | 0x00C8      |         200 |
|      15 | 0x00C9      |         201 |
|      16 | 0x002D      |          45 |
|      17 | 0x0002      |           2 |
|      18 | 0x00D7      |         215 |

## String References

- **7350**: Relinquish your claim to the battle spoils? [Yes./On second thought...]
- **7351**: Items will be lost. Are you certain? [Yes, relinquish./No, retain.]
- **7684**: The threads of space and time warp and bend before your eyes...
- **7685**: Travel to the Walk of Echoes? [Yes, venture forth./No, remain behind.]
- **7686**: You have not claimed all of your battle rewards.

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 97 bytes |
| Instructions | 25       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    48 00 80 23 24 01 80  02 80 02 80 25 02 00 10   H..#$......%...
0010: 02 80 00 4E 00 03 01 10  03 80 43 00 43 01 06 01  ...N......C.C...
0020: 10 42 CD 04 80 F0 FF FF  7F F0 FF FF 7F 6D 61 69  .B...........mai
0030: 6E 02 80 1C 05 80 92 01  F0 FF FF 7F 1C 06 80 1A  n...............
0040: 1A 01 1C 07 80 03 01 10  08 80 30 01 5E 00 02 00  ..........0.^...
0050: 10 08 80 00 5E 00 03 01  10 09 80 01 5E 00 20 00  ....^.......^. .
0060: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x48] [System] [7684*]:
    → "The threads of space and time warp and bend before your eyes..."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x24] CREATE_DIALOG(message_id=7685*, default_option=0*, option_flags=0*)
    → "Travel to the Walk of Echoes? [Yes, venture forth./No, remain behind.]"
  3: 0x000C [0x25] WAIT_DIALOG_SELECT()
  4: 0x000D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x004E
  5: 0x0015 [0x03] Work_Zone[1] = 255*
  6: 0x001A [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  7: 0x001C [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  8: 0x001E [0x06] Work_Zone[1] = 0
  9: 0x0021 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 10: 0x0022 [0xCD] LOAD_SCHEDULED_TASK_ALT4: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[79*, 0*]
 11: 0x0033 [0x1C] WAIT(150* ticks)
 12: 0x0036 [0x92] LocalPlayer->Render.Flags3 ^= 0x01
 13: 0x003C [0x1C] WAIT(40* ticks)
 14: 0x003F [0x1A] CALL_SUBROUTINE(address=0x011A)
 15: 0x0042 [0x1C] WAIT(30* ticks)
 16: 0x0045 [0x03] Work_Zone[1] = 1*
 17: 0x004A [0x30] SET_UCOFF_CONTINUE_ZERO()
 18: 0x004B [0x01] GOTO 0x005E
 19: 0x004E [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x005E
 20: 0x0056 [0x03] Work_Zone[1] = 1073741824*
 21: 0x005B [0x01] GOTO 0x005E

SUBROUTINE_005E:
 22: 0x005E [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 23: 0x0060 [0x21] END_EVENT
 24: 0x0061 [0x00] END_REQSTACK()
```

### Event 23

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0062    |
| Data Size    | 742 bytes |
| Instructions | 20        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:       48 0A 80 1C 06 80  24 0B 80 08 80 02 80 25    H.....$......%
0070: 02 00 10 02 80 00 A3 00  24 0C 80 08 80 02 80 25  ........$......%
0080: 02 00 10 02 80 00 90 00  03 01 10 0D 80 01 A0 00  ................
0090: 02 00 10 08 80 00 A0 00  03 01 10 09 80 01 A0 00  ................
00A0: 01 B3 00 02 00 10 08 80  00 B3 00 03 01 10 09 80  ................
00B0: 01 B3 00 20 00 21 00 45  0E 80 F0 FF FF 7F F0 FF  ... .!.E........
00C0: FF 7F 66 64 69 30 02 80  55 0E 80 F0 FF FF 7F F0  ..fdi0..U.......
00D0: FF FF 7F 66 64 69 30 1B  45 0E 80 F0 FF FF 7F F0  ...fdi0.E.......
00E0: FF FF 7F 66 64 6F 30 02  80 55 0E 80 F0 FF FF 7F  ...fdo0..U......
00F0: F0 FF FF 7F 66 64 6F 30  1B 45 0E 80 F0 FF FF 7F  ....fdo0.E......
0100: F0 FF FF 7F 66 64 69 31  02 80 55 0E 80 F0 FF FF  ....fdi1..U.....
0110: 7F F0 FF FF 7F 66 64 69  31 1B 45 0E 80 F0 FF FF  .....fdi1.E.....
0120: 7F F0 FF FF 7F 66 64 6F  31 02 80 55 0E 80 F0 FF  .....fdo1..U....
0130: FF 7F F0 FF FF 7F 66 64  6F 31 1B 45 0F 80 F0 FF  ......fdo1.E....
0140: FF 7F F0 FF FF 7F 77 68  69 31 02 80 55 0F 80 F0  ......whi1..U...
0150: FF FF 7F F0 FF FF 7F 77  68 69 31 1B 45 0F 80 F0  .......whi1.E...
0160: FF FF 7F F0 FF FF 7F 77  68 6F 31 02 80 55 0F 80  .......who1..U..
0170: F0 FF FF 7F F0 FF FF 7F  77 68 6F 31 1B 45 0F 80  ........who1.E..
0180: F0 FF FF 7F F0 FF FF 7F  77 68 6F 32 02 80 55 0F  ........who2..U.
0190: 80 F0 FF FF 7F F0 FF FF  7F 77 68 6F 32 1B 45 0F  .........who2.E.
01A0: 80 F0 FF FF 7F F0 FF FF  7F 77 68 6F 33 02 80 55  .........who3..U
01B0: 0F 80 F0 FF FF 7F F0 FF  FF 7F 77 68 6F 33 1B 62  ..........who3.b
01C0: 08 80 F0 FF FF 7F F0 FF  FF 7F 6D 61 69 6E 02 80  ..........main..
01D0: 1C 10 80 45 0E 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ...E..........fd
01E0: 6F 31 02 80 55 0E 80 F0  FF FF 7F F0 FF FF 7F 66  o1..U..........f
01F0: 64 6F 31 1B 45 0E 80 F0  FF FF 7F F0 FF FF 7F 66  do1.E..........f
0200: 64 69 31 02 80 62 11 80  F0 FF FF 7F F0 FF FF 7F  di1..b..........
0210: 6D 61 69 6E 02 80 1C 07  80 55 0E 80 F0 FF FF 7F  main.....U......
0220: F0 FF FF 7F 66 64 69 31  1B 45 0E 80 F0 FF FF 7F  ....fdi1.E......
0230: F0 FF FF 7F 62 6C 6F 6E  02 80 45 0F 80 F0 FF FF  ....blon..E.....
0240: 7F F0 FF FF 7F 62 6C 6F  6E 02 80 1B 45 0F 80 F0  .....blon...E...
0250: FF FF 7F F0 FF FF 7F 77  68 69 30 02 80 55 0F 80  .......whi0..U..
0260: F0 FF FF 7F F0 FF FF 7F  77 68 69 30 1B 45 0F 80  ........whi0.E..
0270: F0 FF FF 7F F0 FF FF 7F  77 68 6F 30 02 80 55 0F  ........who0..U.
0280: 80 F0 FF FF 7F F0 FF FF  7F 77 68 6F 30 1B 45 12  .........who0.E.
0290: 80 F0 FF FF 7F F0 FF FF  7F 65 66 6F 6E 02 80 55  .........efon..U
02A0: 12 80 F0 FF FF 7F F0 FF  FF 7F 65 66 6F 6E 1B 45  ..........efon.E
02B0: 0E 80 F0 FF FF 7F F0 FF  FF 7F 66 64 69 73 02 80  ..........fdis..
02C0: 1B 45 0E 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 73  .E..........fdos
02D0: 02 80 55 0E 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..U..........fdo
02E0: 73 1B 45 0E 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  s.E..........fdi
02F0: 66 02 80 1B 45 0E 80 F0  FF FF 7F F0 FF FF 7F 66  f...E..........f
0300: 64 6F 66 02 80 55 0E 80  F0 FF FF 7F F0 FF FF 7F  dof..U..........
0310: 66 64 6F 66 1B 45 0E 80  F0 FF FF 7F F0 FF FF 7F  fdof.E..........
0320: 66 64 69 70 02 80 1B 45  0E 80 F0 FF FF 7F F0 FF  fdip...E........
0330: FF 7F 66 64 6F 70 02 80  55 0E 80 F0 FF FF 7F F0  ..fdop..U.......
0340: FF FF 7F 66 64 6F 70 1B                           ...fdop.        
```

#### Opcodes

```
  0: 0x0062 [0x48] [System] [7686*]:
    → "You have not claimed all of your battle rewards."
  1: 0x0065 [0x1C] WAIT(40* ticks)
  2: 0x0068 [0x24] CREATE_DIALOG(message_id=7350*, default_option=1*, option_flags=0*)
    → "Relinquish your claim to the battle spoils? [Yes./On second thought...]"
  3: 0x006F [0x25] WAIT_DIALOG_SELECT()
  4: 0x0070 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00A3
  5: 0x0078 [0x24] CREATE_DIALOG(message_id=7351*, default_option=1*, option_flags=0*)
    → "Items will be lost. Are you certain? [Yes, relinquish./No, retain.]"
  6: 0x007F [0x25] WAIT_DIALOG_SELECT()
  7: 0x0080 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0090
  8: 0x0088 [0x03] Work_Zone[1] = 10*
  9: 0x008D [0x01] GOTO 0x00A0
 10: 0x0090 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00A0
 11: 0x0098 [0x03] Work_Zone[1] = 1073741824*
 12: 0x009D [0x01] GOTO 0x00A0

SUBROUTINE_00A0:
 13: 0x00A0 [0x01] GOTO 0x00B3
 14: 0x00A3 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00B3
 15: 0x00AB [0x03] Work_Zone[1] = 1073741824*
 16: 0x00B0 [0x01] GOTO 0x00B3

SUBROUTINE_00B3:
 17: 0x00B3 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 18: 0x00B5 [0x21] END_EVENT
 19: 0x00B6 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00B7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x00C8 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=200*
     0x00D7 [0x1B] RETURN
     0x00D8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x00E9 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=200*
     0x00F8 [0x1B] RETURN
     0x00F9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x010A [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0119 [0x1B] RETURN
     0x011A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x012B [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x013A [0x1B] RETURN
     0x013B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x014C [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=201*
     0x015B [0x1B] RETURN
     0x015C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x016D [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=201*
     0x017C [0x1B] RETURN
     0x017D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who2" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x018E [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who2" with entities [LocalPlayer, LocalPlayer], work=201*
     0x019D [0x1B] RETURN
     0x019E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who3" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x01AF [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who3" with entities [LocalPlayer, LocalPlayer], work=201*
     0x01BE [0x1B] RETURN
     0x01BF [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
     0x01D0 [0x1C] WAIT(45* ticks)
     0x01D3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x01E4 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x01F3 [0x1B] RETURN
     0x01F4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0205 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[2*, 0*]
     0x0216 [0x1C] WAIT(30* ticks)
     0x0219 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0228 [0x1B] RETURN
     0x0229 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x023A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x024B [0x1B] RETURN
     0x024C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi0" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x025D [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "whi0" with entities [LocalPlayer, LocalPlayer], work=201*
     0x026C [0x1B] RETURN
     0x026D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who0" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x027E [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who0" with entities [LocalPlayer, LocalPlayer], work=201*
     0x028D [0x1B] RETURN
     0x028E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "efon" with entities [LocalPlayer, LocalPlayer], work=[215*, 0*]
     0x029F [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "efon" with entities [LocalPlayer, LocalPlayer], work=215*
     0x02AE [0x1B] RETURN
     0x02AF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdis" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x02C0 [0x1B] RETURN
     0x02C1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdos" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x02D2 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdos" with entities [LocalPlayer, LocalPlayer], work=200*
     0x02E1 [0x1B] RETURN
     0x02E2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdif" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x02F3 [0x1B] RETURN
     0x02F4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0305 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdof" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0314 [0x1B] RETURN
     0x0315 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdip" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0326 [0x1B] RETURN
     0x0327 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdop" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0338 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdop" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0347 [0x1B] RETURN
```
