# 17809549 - Nashmeira

## Common Data

| Field            | Value          |
|------------------|----------------|
| Zone             | Norg (ID: 252) |
| Block Size       | 148 bytes      |
| Total Events     | 5              |
| References Count | 7              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     29 |              4 |
| [65535.2](#event-655352) | 0x001E       |     29 |              4 |
| [290](#event-290)        | 0x003B       |      1 |              1 |
| [65535.3](#event-655353) | 0x003C       |     22 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0606      |        1542 |
|       1 | 0x0638      |        1592 |
|       2 | 0x0028      |          40 |
|       3 | 0x1AFF9     |      110585 |
|       4 | 0xFFFFD8E0  |  4294957280 |
|       5 | 0xFFFFE452  |  4294960210 |
|       6 | 0x001E      |          30 |

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 29 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    B4 00 00 00 41 70 68  6D 61 75 00 00 00 00 00   ....Aphmau.....
0010: 00 00 00 00 00 B5 00 00  00 B6 00 00 80 00        ..............  
```

#### Opcodes

```
  0: 0x0001 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x00 - Copy string from opcode, work_offset=ExtData[1]->WorkLocal[0], string="Aphmau")
  1: 0x0015 [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x0019 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=1542*)
  3: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001E   |
| Data Size    | 29 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            B4 00                ..
0020: 00 00 4E 61 73 68 6D 65  69 72 61 00 00 00 00 00  ..Nashmeira.....
0030: 00 00 B5 00 00 00 B6 00  01 80 00                 ...........     
```

#### Opcodes

```
  0: 0x001E [0xB4] UI_WINDOW_STRING_HANDLER(case=0x00 - Copy string from opcode, work_offset=ExtData[1]->WorkLocal[0], string="Nashmeira")
  1: 0x0032 [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x0036 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=1592*)
  3: 0x003A [0x00] END_REQSTACK()
```

### Event 290

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   00                         .    
```

#### Opcodes

```
  0: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      32 02 80 1F              2...
0040: 00 03 80 04 80 05 80 1F  01 1E F0 FF FF 7F 1C 06  ................
0050: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x003C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x003F [0x1F] MOVE_ENTITY: EventEntity moves to X=110.585*, Z=-10.016*, Y=-7.086*
  2: 0x0047 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0049 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x004E [0x1C] WAIT(30* ticks)
  5: 0x0051 [0x00] END_REQSTACK()
```
