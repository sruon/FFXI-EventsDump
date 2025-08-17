# 17863406 - Donda-Bonda

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Morimar Basalt Fields (ID: 265) |
| Block Size       | 236 bytes                       |
| Total Events     | 5                               |
| References Count | 17                              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [58](#event-58)          | 0x0001       |      7 |              2 |
| [62](#event-62)          | 0x0008       |     51 |              5 |
| [65535.1](#event-655351) | 0x003B       |     22 |              6 |
| [65535.2](#event-655352) | 0x0051       |     50 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x0039      |          57 |
|       3 | 0x0018      |          24 |
|       4 | 0x0014      |          20 |
|       5 | 0x0073      |         115 |
|       6 | 0x0028      |          40 |
|       7 | 0x6BA18     |      440856 |
|       8 | 0xFFFAB0F5  |  4294619381 |
|       9 | 0xFFFFC312  |  4294951698 |
|      10 | 0x001E      |          30 |
|      11 | 0x0005      |           5 |
|      12 | 0x0004      |           4 |
|      13 | 0x005E      |          94 |
|      14 | 0x0008      |           8 |
|      15 | 0x0066      |         102 |
|      16 | 0x0054      |          84 |

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

### Event 58

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 62

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0008   |
| Data Size    | 51 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          B4 00 00 00 4F 74 68 65          ....Othe
0010: 6C 6C 69 75 73 00 00 00  00 00 00 00 B5 00 00 00  llius...........
0020: B6 0B 00 80 01 80 01 80  02 80 03 80 04 80 05 80  ................
0030: 01 80 01 80 92 01 F8 FF  FF 7F 00                 ...........     
```

#### Opcodes

```
  0: 0x0008 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x00 - Copy string from opcode, work_offset=ExtData[1]->WorkLocal[0], string="Othellius")
  1: 0x001C [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x0020 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=1*, hair=0*, head=0*, body=57*, hands=24*, legs=20*, feet=115*, main=0*, sub=0*)
  3: 0x0034 [0x92] EventEntity->Render.Flags3 ^= 0x01
  4: 0x003A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   32 06 80 1F 00             2....
0040: 07 80 08 80 09 80 1F 01  1E ED 92 10 01 1C 0A 80  ................
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x003B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x003E [0x1F] MOVE_ENTITY: EventEntity moves to X=440.856*, Z=-347.915*, Y=-15.598*
  2: 0x0046 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0048 [0x1E] EventEntity looks at Borghest (ID: 17863405/0x011092ED) and starts talking
  4: 0x004D [0x1C] WAIT(30* ticks)
  5: 0x0050 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0051   |
| Data Size    | 50 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    B4 00 00 00 44 6F 6E  64 61 2D 42 6F 6E 64 61   ....Donda-Bonda
0060: 00 00 00 00 00 B5 00 00  00 B6 0B 0B 80 0C 80 01  ................
0070: 80 0D 80 0E 80 0F 80 0D  80 10 80 01 80 80 F8 FF  ................
0080: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x0051 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x00 - Copy string from opcode, work_offset=ExtData[1]->WorkLocal[0], string="Donda-Bonda")
  1: 0x0065 [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x0069 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=5*, hair=4*, head=0*, body=94*, hands=8*, legs=102*, feet=94*, main=84*, sub=0*)
  3: 0x007D [0x80] LOAD_WAIT(entity=EventEntity)
  4: 0x0082 [0x00] END_REQSTACK()
```
