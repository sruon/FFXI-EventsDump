# 17134043 - Bottomless Gorge

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Bastok Markets [S] (ID: 87) |
| Block Size       | 316 bytes                   |
| Total Events     | 8                           |
| References Count | 11                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [150](#event-150)        | 0x0001       |     33 |              9 |
| [120](#event-120)        | 0x0022       |      7 |              2 |
| [65535.1](#event-655351) | 0x0029       |    139 |             13 |
| [56](#event-56)          | 0x00B4       |      7 |              2 |
| [60](#event-60)          | 0x00BB       |      7 |              2 |
| [65535.2](#event-655352) | 0x00C2       |     14 |              4 |
| [65535.3](#event-655353) | 0x00D0       |     13 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0045      |          69 |
|       2 | 0x3039      |       12345 |
|       3 | 0x303A      |       12346 |
|       4 | 0x0037      |          55 |
|       5 | 0x003C      |          60 |
|       6 | 0x0028      |          40 |
|       7 | 0x5DD6E     |      384366 |
|       8 | 0x2A124     |      172324 |
|       9 | 0x092A      |        2346 |
|      10 | 0x002B      |          43 |

## String References

- **12345**: This is the Freidrich Battery. It bears the name of President Freidrich, our great leader during the First Battle of Konschtat.
- **12346**: The battery has been reinforced with the finest Bastokan artillery to repel the siege of the beasthordes.

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

### Event 150

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 33 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 66 01 80 F8 FF FF 7F   ........f......
0010: F8 FF FF 7F 74 6C 6B 30  1D 02 80 23 1D 03 80 23  ....tlk0...#...#
0020: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(30* ticks)
  2: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=69*
  3: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=12345*)
    → "This is the Freidrich Battery. It bears the name of President Freidrich, our great leader during the First Battle of Konschtat."
  4: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=12346*)
    → "The battery has been reinforced with the finest Bastokan artillery to repel the siege of the beasthordes."
  6: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0020 [0x21] END_EVENT
  8: 0x0021 [0x00] END_REQSTACK()
```

### Event 120

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0022  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       92 01 F8 FF FF 7F  00                         .......       
```

#### Opcodes

```
  0: 0x0022 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0028 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0029    |
| Data Size    | 139 bytes |
| Instructions | 13        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             1C 00 80 66 01 80 DB           ...f...
0030: 71 05 01 DB 71 05 01 74  6C 6B 31 66 01 80 D6 71  q...q..tlk1f...q
0040: 05 01 D6 71 05 01 74 68  6B 32 5B 04 80 DA 71 05  ...q..thk2[...q.
0050: 01 DA 71 05 01 74 68 61  32 66 05 80 EB 71 05 01  ..q..tha2f...q..
0060: EB 71 05 01 74 68 6B 32  53 D6 71 05 01 D6 71 05  .q..thk2S.q...q.
0070: 01 74 68 6B 32 4A DB 71  05 01 F0 71 05 01 4A D6  .thk2J.q...q..J.
0080: 71 05 01 F0 71 05 01 53  DA 71 05 01 DA 71 05 01  q...q..S.q...q..
0090: 74 68 61 32 4A DA 71 05  01 F0 71 05 01 53 EB 71  tha2J.q...q..S.q
00A0: 05 01 EB 71 05 01 74 68  6B 32 4A EB 71 05 01 F0  ...q..thk2J.q...
00B0: 71 05 01 00                                       q...            
```

#### Opcodes

```
  0: 0x0029 [0x1C] WAIT(30* ticks)
  1: 0x002C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Bottomless Gorge (ID: 17134043/0x010571DB), Bottomless Gorge (ID: 17134043/0x010571DB)], work=69*
  2: 0x003B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [Biggorf (ID: 17134038/0x010571D6), Biggorf (ID: 17134038/0x010571D6)], work=69*
  3: 0x004A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tha2" with entities [Drangord (ID: 17134042/0x010571DA), Drangord (ID: 17134042/0x010571DA)], work=55*
  4: 0x0059 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [Dunbaff (ID: 17134059/0x010571EB), Dunbaff (ID: 17134059/0x010571EB)], work=60*
  5: 0x0068 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [Biggorf (ID: 17134038/0x010571D6), Biggorf (ID: 17134038/0x010571D6)]
  6: 0x0075 [0x4A] Bottomless Gorge (ID: 17134043/0x010571DB) looks at Pale Eagle (ID: 17134064/0x010571F0)
  7: 0x007E [0x4A] Biggorf (ID: 17134038/0x010571D6) looks at Pale Eagle (ID: 17134064/0x010571F0)
  8: 0x0087 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tha2" with entities [Drangord (ID: 17134042/0x010571DA), Drangord (ID: 17134042/0x010571DA)]
  9: 0x0094 [0x4A] Drangord (ID: 17134042/0x010571DA) looks at Pale Eagle (ID: 17134064/0x010571F0)
 10: 0x009D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [Dunbaff (ID: 17134059/0x010571EB), Dunbaff (ID: 17134059/0x010571EB)]
 11: 0x00AA [0x4A] Dunbaff (ID: 17134059/0x010571EB) looks at Pale Eagle (ID: 17134064/0x010571F0)
 12: 0x00B3 [0x00] END_REQSTACK()
```

### Event 56

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B4  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:             92 01 F8 FF  FF 7F 00                     .......     
```

#### Opcodes

```
  0: 0x00B4 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00BA [0x00] END_REQSTACK()
```

### Event 60

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00BB  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                   92 01 F8 FF FF             .....
00C0: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x00BB [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00C1 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C2   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:       32 06 80 1F 00 07  80 08 80 09 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x00C2 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00C5 [0x1F] MOVE_ENTITY: EventEntity moves to X=384.366*, Z=172.324*, Y=2.346*
  2: 0x00CD [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00CF [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D0   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0: 6E F8 FF FF 7F 0A 80 99  F8 FF FF 7F 00           n............   
```

#### Opcodes

```
  0: 0x00D0 [0x6E] EventEntity uses emote 43*
  1: 0x00D7 [0x99] Wait for EventEntity animation to complete
  2: 0x00DC [0x00] END_REQSTACK()
```
