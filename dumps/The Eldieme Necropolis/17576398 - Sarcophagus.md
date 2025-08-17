# 17576398 - Sarcophagus

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | The Eldieme Necropolis (ID: 195) |
| Block Size       | 444 bytes                        |
| Total Events     | 2                                |
| References Count | 11                               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [46](#event-46)       | 0x0001       |    374 |             43 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x0013      |          19 |
|       3 | 0x00D0      |         208 |
|       4 | 0x0320      |         800 |
|       5 | 0x001E      |          30 |
|       6 | 0x1D1C      |        7452 |
|       7 | 0x0003      |           3 |
|       8 | 0x003C      |          60 |
|       9 | 0x0040      |          64 |
|      10 | 0x0078      |         120 |

## String References

- **7452**: You play the requiem for the soul that sleeps in this sarcophagus.

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

### Event 46

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 374 bytes |
| Instructions | 43        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    2F 00 D0 31 0C 01 20  01 46 01 42 45 00 80 F0   /..1.. .F.BE...
0010: FF FF 7F F0 FF FF 7F 66  64 6F 31 01 80 55 00 80  .......fdo1..U..
0020: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 38 02 80 79  ........fdo18..y
0030: 00 F0 FF FF 7F F0 FF FF  7F 29 03 F0 FF FF 7F 06  .........)......
0040: 29 03 D0 31 0C 01 02 79  00 D0 31 0C 01 F0 FF FF  )..1...y..1.....
0050: 7F 4E 00 D0 31 0C 01 6C  D0 31 0C 01 01 80 01 80  .N..1..l.1......
0060: 45 03 80 F0 FF FF 7F F0  FF FF 7F 75 30 30 32 01  E..........u002.
0070: 80 55 03 80 F0 FF FF 7F  F0 FF FF 7F 75 30 30 32  .U..........u002
0080: 45 00 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 31 01  E..........fdi1.
0090: 80 55 00 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 31  .U..........fdi1
00A0: 45 03 80 F0 FF FF 7F F0  FF FF 7F 75 30 30 30 01  E..........u000.
00B0: 80 2C F0 FF FF 7F F0 FF  FF 7F 6C 63 30 30 1C 04  .,........lc00..
00C0: 80 55 03 80 F0 FF FF 7F  F0 FF FF 7F 75 30 30 30  .U..........u000
00D0: 6B 69 64 6C 30 F0 FF FF  7F 1C 05 80 48 06 80 23  kidl0.......H..#
00E0: 62 07 80 F8 FF FF 7F F8  FF FF 7F 6D 61 69 6E 01  b..........main.
00F0: 80 1C 08 80 27 03 D0 31  0C 01 03 1C 09 80 79 00  ....'..1......y.
0100: F0 FF FF 7F D0 31 0C 01  2A 03 D0 31 0C 01 1C 0A  .....1..*..1....
0110: 80 45 03 80 F0 FF FF 7F  F0 FF FF 7F 75 30 30 31  .E..........u001
0120: 01 80 55 03 80 F0 FF FF  7F F0 FF FF 7F 75 30 30  ..U..........u00
0130: 31 1C 05 80 29 04 D0 31  0C 01 04 29 03 D0 31 0C  1...)..1...)..1.
0140: 01 05 45 00 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..E..........fdo
0150: 32 01 80 55 00 80 F0 FF  FF 7F F0 FF FF 7F 66 64  2..U..........fd
0160: 6F 32 46 00 45 00 80 F0  FF FF 7F F0 FF FF 7F 66  o2F.E..........f
0170: 64 69 32 01 80 21 00                              di2..!.         
```

#### Opcodes

```
  0: 0x0001 [0x2F] Unnamed NPC (ID: 17576400/0x010C31D0)->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x0007 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x0009 [0x46] CAMERA_CONTROL: Disable user control
  3: 0x000B [0x42] SET_CLI_EVENT_CANCEL_DATA()
  4: 0x000C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  5: 0x001D [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  6: 0x002C [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  7: 0x002F [0x79] LocalPlayer looks at LocalPlayer (Basic look)
  8: 0x0039 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=LocalPlayer, tag_num=0x06)
  9: 0x0040 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Unnamed NPC (ID: 17576400/0x010C31D0), tag_num=0x02)
 10: 0x0047 [0x79] Unnamed NPC (ID: 17576400/0x010C31D0) looks at LocalPlayer (Basic look)
 11: 0x0051 [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17576400/0x010C31D0)
 12: 0x0057 [0x6C] FADE_ENTITY_COLOR(entity_id=Unnamed NPC (ID: 17576400/0x010C31D0), end_alpha=0*, fade_time=0*)
 13: 0x0060 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "u002" with entities [LocalPlayer, LocalPlayer], work=[208*, 0*]
 14: 0x0071 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "u002" with entities [LocalPlayer, LocalPlayer], work=208*
 15: 0x0080 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x0091 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 17: 0x00A0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "u000" with entities [LocalPlayer, LocalPlayer], work=[208*, 0*]
 18: 0x00B1 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "lc00" with entities [LocalPlayer, LocalPlayer]
 19: 0x00BE [0x1C] WAIT(800* ticks)
 20: 0x00C1 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "u000" with entities [LocalPlayer, LocalPlayer], work=208*
 21: 0x00D0 [0x6B] STOP_AND_IDLE: LocalPlayer stops current action and resets to idle (animation="idl0")
 22: 0x00D9 [0x1C] WAIT(30* ticks)
 23: 0x00DC [0x48] [System] [7452*]:
    → "You play the requiem for the soul that sleeps in this sarcophagus."
 24: 0x00DF [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x00E0 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [EventEntity, EventEntity], work=[3*, 0*]
 26: 0x00F1 [0x1C] WAIT(60* ticks)
 27: 0x00F4 [0x27] REQ_SET(priority=0x03, entity_id=Unnamed NPC (ID: 17576400/0x010C31D0), tag_num=0x03)
 28: 0x00FB [0x1C] WAIT(64* ticks)
 29: 0x00FE [0x79] LocalPlayer looks at Unnamed NPC (ID: 17576400/0x010C31D0) (Basic look)
 30: 0x0108 [0x2A] GET_REQ_LEVEL(level=3, entity_id=Unnamed NPC (ID: 17576400/0x010C31D0))
 31: 0x010E [0x1C] WAIT(120* ticks)
 32: 0x0111 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "u001" with entities [LocalPlayer, LocalPlayer], work=[208*, 0*]
 33: 0x0122 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "u001" with entities [LocalPlayer, LocalPlayer], work=208*
 34: 0x0131 [0x1C] WAIT(30* ticks)
 35: 0x0134 [0x29] REQ_SET_WAIT(priority=0x04, entity_id=Unnamed NPC (ID: 17576400/0x010C31D0), tag_num=0x04)
 36: 0x013B [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Unnamed NPC (ID: 17576400/0x010C31D0), tag_num=0x05)
 37: 0x0142 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 38: 0x0153 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=200*
 39: 0x0162 [0x46] CAMERA_CONTROL: Restore default settings
 40: 0x0164 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 41: 0x0175 [0x21] END_EVENT
 42: 0x0176 [0x00] END_REQSTACK()
```
