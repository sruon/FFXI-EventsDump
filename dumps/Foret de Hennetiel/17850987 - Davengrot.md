# 17850987 - Davengrot

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Foret de Hennetiel (ID: 262) |
| Block Size       | 248 bytes                    |
| Total Events     | 7                            |
| References Count | 11                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [519](#event-519)        | 0x0001       |      1 |              1 |
| [521](#event-521)        | 0x0002       |      1 |              1 |
| [527](#event-527)        | 0x0003       |     45 |              4 |
| [528](#event-528)        | 0x0030       |     45 |              4 |
| [65535.1](#event-655351) | 0x005D       |     21 |              2 |
| [65535.2](#event-655352) | 0x0072       |     45 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0003      |           3 |
|       2 | 0x0000      |           0 |
|       3 | 0x0069      |         105 |
|       4 | 0x0008      |           8 |
|       5 | 0x0066      |         102 |
|       6 | 0x0015      |          21 |
|       7 | 0x0056      |          86 |
|       8 | 0x000C      |          12 |
|       9 | 0x0021      |          33 |
|      10 | 0x00A4      |         164 |

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

### Event 519

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 521

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 527

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 45 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          B4 00 00 00 4C  6F 67 61 6E 00 00 00 00     ....Logan....
0010: 00 00 00 00 00 00 00 B5  00 00 00 B6 0B 00 80 01  ................
0020: 80 02 80 03 80 04 80 05  80 06 80 07 80 02 80 00  ................
```

#### Opcodes

```
  0: 0x0003 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x00 - Copy string from opcode, work_offset=ExtData[1]->WorkLocal[0], string="Logan")
  1: 0x0017 [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x001B [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=1*, hair=3*, head=0*, body=105*, hands=8*, legs=102*, feet=21*, main=86*, sub=0*)
  3: 0x002F [0x00] END_REQSTACK()
```

### Event 528

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 45 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: B4 00 00 00 4C 6F 67 61  6E 00 00 00 00 00 00 00  ....Logan.......
0040: 00 00 00 00 B5 00 00 00  B6 0B 00 80 01 80 02 80  ................
0050: 03 80 04 80 05 80 06 80  02 80 02 80 00           .............   
```

#### Opcodes

```
  0: 0x0030 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x00 - Copy string from opcode, work_offset=ExtData[1]->WorkLocal[0], string="Logan")
  1: 0x0044 [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x0048 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=1*, hair=3*, head=0*, body=105*, hands=8*, legs=102*, feet=21*, main=0*, sub=0*)
  3: 0x005C [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005D   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         B6 0B 00               ...
0060: 80 01 80 02 80 03 80 04  80 05 80 06 80 02 80 02  ................
0070: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x005D [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=1*, hair=3*, head=0*, body=105*, hands=8*, legs=102*, feet=21*, main=0*, sub=0*)
  1: 0x0071 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0072   |
| Data Size    | 45 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       B4 00 00 00 44 61  76 65 6E 67 72 6F 74 00    ....Davengrot.
0080: 00 00 00 00 00 00 B5 00  00 00 B6 0B 00 80 08 80  ................
0090: 02 80 09 80 05 80 0A 80  0A 80 02 80 02 80 00     ............... 
```

#### Opcodes

```
  0: 0x0072 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x00 - Copy string from opcode, work_offset=ExtData[1]->WorkLocal[0], string="Davengrot")
  1: 0x0086 [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x008A [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=1*, hair=12*, head=0*, body=33*, hands=102*, legs=164*, feet=164*, main=0*, sub=0*)
  3: 0x009E [0x00] END_REQSTACK()
```
