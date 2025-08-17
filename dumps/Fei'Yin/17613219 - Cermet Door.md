# 17613219 - Cermet Door

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Fei'Yin (ID: 204) |
| Block Size       | 812 bytes         |
| Total Events     | 6                 |
| References Count | 12                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [40](#event-40)          | 0x0001       |    713 |             77 |
| [42](#event-42)          | 0x02CA       |      2 |              2 |
| [43](#event-43)          | 0x02CC       |      2 |              2 |
| [65535.1](#event-655351) | 0x02CE       |      2 |              2 |
| [65535.2](#event-655352) | 0x02D0       |      2 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0002      |           2 |
|       1 | 0x0000      |           0 |
|       2 | 0x2710      |       10000 |
|       3 | 0x21EF8     |      139000 |
|       4 | 0xFFFFFC01  |  4294966273 |
|       5 | 0x00F0      |         240 |
|       6 | 0x0001      |           1 |
|       7 | 0x00C8      |         200 |
|       8 | 0x00C9      |         201 |
|       9 | 0x002D      |          45 |
|      10 | 0x001E      |          30 |
|      11 | 0x00D7      |         215 |

## String References

- **2**: Pass through the door? [Yes./No.]

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

### Event 40

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 713 bytes |
| Instructions | 22        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    24 00 80 01 80 01 80  25 02 00 10 01 80 00 2C   $......%......,
0010: 00 42 1A 9C 00 4C 47 00  02 80 03 80 01 80 04 80  .B...LG.........
0020: 47 01 1C 05 80 4D 1A 7B  00 01 37 00 02 00 10 06  G....M.{..7.....
0030: 80 00 37 00 01 37 00 21  00 45 07 80 F0 FF FF 7F  ..7..7.!.E......
0040: F0 FF FF 7F 66 64 69 30  01 80 55 07 80 F0 FF FF  ....fdi0..U.....
0050: 7F F0 FF FF 7F 66 64 69  30 1B 45 07 80 F0 FF FF  .....fdi0.E.....
0060: 7F F0 FF FF 7F 66 64 6F  30 01 80 55 07 80 F0 FF  .....fdo0..U....
0070: FF 7F F0 FF FF 7F 66 64  6F 30 1B 45 07 80 F0 FF  ......fdo0.E....
0080: FF 7F F0 FF FF 7F 66 64  69 31 01 80 55 07 80 F0  ......fdi1..U...
0090: FF FF 7F F0 FF FF 7F 66  64 69 31 1B 45 07 80 F0  .......fdi1.E...
00A0: FF FF 7F F0 FF FF 7F 66  64 6F 31 01 80 55 07 80  .......fdo1..U..
00B0: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 1B 45 08 80  ........fdo1.E..
00C0: F0 FF FF 7F F0 FF FF 7F  77 68 69 31 01 80 55 08  ........whi1..U.
00D0: 80 F0 FF FF 7F F0 FF FF  7F 77 68 69 31 1B 45 08  .........whi1.E.
00E0: 80 F0 FF FF 7F F0 FF FF  7F 77 68 6F 31 01 80 55  .........who1..U
00F0: 08 80 F0 FF FF 7F F0 FF  FF 7F 77 68 6F 31 1B 45  ..........who1.E
0100: 08 80 F0 FF FF 7F F0 FF  FF 7F 77 68 6F 32 01 80  ..........who2..
0110: 55 08 80 F0 FF FF 7F F0  FF FF 7F 77 68 6F 32 1B  U..........who2.
0120: 45 08 80 F0 FF FF 7F F0  FF FF 7F 77 68 6F 33 01  E..........who3.
0130: 80 55 08 80 F0 FF FF 7F  F0 FF FF 7F 77 68 6F 33  .U..........who3
0140: 1B 62 06 80 F0 FF FF 7F  F0 FF FF 7F 6D 61 69 6E  .b..........main
0150: 01 80 1C 09 80 45 07 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
0160: 66 64 6F 31 01 80 55 07  80 F0 FF FF 7F F0 FF FF  fdo1..U.........
0170: 7F 66 64 6F 31 1B 45 07  80 F0 FF FF 7F F0 FF FF  .fdo1.E.........
0180: 7F 66 64 69 31 01 80 62  00 80 F0 FF FF 7F F0 FF  .fdi1..b........
0190: FF 7F 6D 61 69 6E 01 80  1C 0A 80 55 07 80 F0 FF  ..main.....U....
01A0: FF 7F F0 FF FF 7F 66 64  69 31 1B 45 07 80 F0 FF  ......fdi1.E....
01B0: FF 7F F0 FF FF 7F 62 6C  6F 6E 01 80 45 08 80 F0  ......blon..E...
01C0: FF FF 7F F0 FF FF 7F 62  6C 6F 6E 01 80 1B 45 08  .......blon...E.
01D0: 80 F0 FF FF 7F F0 FF FF  7F 77 68 69 30 01 80 55  .........whi0..U
01E0: 08 80 F0 FF FF 7F F0 FF  FF 7F 77 68 69 30 1B 45  ..........whi0.E
01F0: 08 80 F0 FF FF 7F F0 FF  FF 7F 77 68 6F 30 01 80  ..........who0..
0200: 55 08 80 F0 FF FF 7F F0  FF FF 7F 77 68 6F 30 1B  U..........who0.
0210: 45 0B 80 F0 FF FF 7F F0  FF FF 7F 65 66 6F 6E 01  E..........efon.
0220: 80 55 0B 80 F0 FF FF 7F  F0 FF FF 7F 65 66 6F 6E  .U..........efon
0230: 1B 45 07 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 73  .E..........fdis
0240: 01 80 1B 45 07 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ...E..........fd
0250: 6F 73 01 80 55 07 80 F0  FF FF 7F F0 FF FF 7F 66  os..U..........f
0260: 64 6F 73 1B 45 07 80 F0  FF FF 7F F0 FF FF 7F 66  dos.E..........f
0270: 64 69 66 01 80 1B 45 07  80 F0 FF FF 7F F0 FF FF  dif...E.........
0280: 7F 66 64 6F 66 01 80 55  07 80 F0 FF FF 7F F0 FF  .fdof..U........
0290: FF 7F 66 64 6F 66 1B 45  07 80 F0 FF FF 7F F0 FF  ..fdof.E........
02A0: FF 7F 66 64 69 70 01 80  1B 45 07 80 F0 FF FF 7F  ..fdip...E......
02B0: F0 FF FF 7F 66 64 6F 70  01 80 55 07 80 F0 FF FF  ....fdop..U.....
02C0: 7F F0 FF FF 7F 66 64 6F  70 1B                    .....fdop.      
```

#### Opcodes

```
  0: 0x0001 [0x24] CREATE_DIALOG(message_id=2*, default_option=0*, option_flags=0*)
    → "Pass through the door? [Yes./No.]"
  1: 0x0008 [0x25] WAIT_DIALOG_SELECT()
  2: 0x0009 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x002C
  3: 0x0011 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  4: 0x0012 [0x1A] CALL_SUBROUTINE(address=0x009C)
  5: 0x0015 [0x4C] EventEntity->StatusEvent = 8 // Open door
  6: 0x0016 [0x47] UPDATE_PLAYER_POS(10.000*, 139.000*, 0.000*, yaw=377476129.3°*)
  7: 0x0020 [0x47] WAIT_PLAYER_POS_UPDATE
  8: 0x0022 [0x1C] WAIT(240* ticks)
  9: 0x0025 [0x4D] EventEntity->StatusEvent = 9 // Close door
 10: 0x0026 [0x1A] CALL_SUBROUTINE(address=0x007B)
 11: 0x0029 [0x01] GOTO 0x0037
 12: 0x002C [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0037
 13: 0x0034 [0x01] GOTO 0x0037

SUBROUTINE_0037:
 14: 0x0037 [0x21] END_EVENT
 15: 0x0038 [0x00] END_REQSTACK()

SUBROUTINE_007B:
 16: 0x007B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 17: 0x008C [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 18: 0x009B [0x1B] RETURN

SUBROUTINE_009C:
 19: 0x009C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x00AD [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 21: 0x00BC [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0039 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x004A [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0059 [0x1B] RETURN
     0x005A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x006B [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=200*
     0x007A [0x1B] RETURN
# Dead code (unreachable instructions):
     0x00BD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x00CE [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=201*
     0x00DD [0x1B] RETURN
     0x00DE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x00EF [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=201*
     0x00FE [0x1B] RETURN
     0x00FF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who2" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0110 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who2" with entities [LocalPlayer, LocalPlayer], work=201*
     0x011F [0x1B] RETURN
     0x0120 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who3" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0131 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who3" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0140 [0x1B] RETURN
     0x0141 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
     0x0152 [0x1C] WAIT(45* ticks)
     0x0155 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0166 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0175 [0x1B] RETURN
     0x0176 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0187 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[2*, 0*]
     0x0198 [0x1C] WAIT(30* ticks)
     0x019B [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x01AA [0x1B] RETURN
     0x01AB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x01BC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x01CD [0x1B] RETURN
     0x01CE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi0" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x01DF [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "whi0" with entities [LocalPlayer, LocalPlayer], work=201*
     0x01EE [0x1B] RETURN
     0x01EF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who0" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x0200 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who0" with entities [LocalPlayer, LocalPlayer], work=201*
     0x020F [0x1B] RETURN
     0x0210 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "efon" with entities [LocalPlayer, LocalPlayer], work=[215*, 0*]
     0x0221 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "efon" with entities [LocalPlayer, LocalPlayer], work=215*
     0x0230 [0x1B] RETURN
     0x0231 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdis" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0242 [0x1B] RETURN
     0x0243 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdos" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0254 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdos" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0263 [0x1B] RETURN
     0x0264 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdif" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0275 [0x1B] RETURN
     0x0276 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0287 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdof" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0296 [0x1B] RETURN
     0x0297 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdip" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x02A8 [0x1B] RETURN
     0x02A9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdop" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x02BA [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdop" with entities [LocalPlayer, LocalPlayer], work=200*
     0x02C9 [0x1B] RETURN
```

### Event 42

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x02CA  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02C0:                                4D 00                        M.    
```

#### Opcodes

```
  0: 0x02CA [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x02CB [0x00] END_REQSTACK()
```

### Event 43

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x02CC  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02C0:                                      4D 00                    M.  
```

#### Opcodes

```
  0: 0x02CC [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x02CD [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x02CE  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02C0:                                            4C 00                L.
```

#### Opcodes

```
  0: 0x02CE [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x02CF [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x02D0  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02D0: 4D 00                                             M.              
```

#### Opcodes

```
  0: 0x02D0 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x02D1 [0x00] END_REQSTACK()
```
