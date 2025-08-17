# 17855049 - Vortimere

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Yorcia Weald (ID: 263) |
| Block Size       | 168 bytes              |
| Total Events     | 6                      |
| References Count | 6                      |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [114](#event-114)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     14 |              4 |
| [122](#event-122)        | 0x0010       |     29 |              4 |
| [123](#event-123)        | 0x002D       |     29 |              4 |
| [65535.2](#event-655352) | 0x004A       |     29 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x3F416     |      259094 |
|       2 | 0x5EE47     |      388679 |
|       3 | 0xFFFFF835  |  4294965301 |
|       4 | 0x0108      |         264 |
|       5 | 0x0A91      |        2705 |

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

### Event 114

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=259.094*, Z=388.679*, Y=-1.995*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x00] END_REQSTACK()
```

### Event 122

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 29 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: B6 00 04 80 B4 13 00 00  4A 6F 76 69 61 6C 40 41  ........Jovial@A
0020: 68 72 69 6D 61 6E 00 00  B5 00 00 00 00           hriman.......   
```

#### Opcodes

```
  0: 0x0010 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=264*)
  1: 0x0014 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x13 - Copy string and replace @ with space, work_offset=ExtData[1]->WorkLocal[0], string="Jovial@Ahriman")
  2: 0x0028 [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  3: 0x002C [0x00] END_REQSTACK()
```

### Event 123

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 29 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         B6 00 04               ...
0030: 80 B4 13 00 00 4A 6F 76  69 61 6C 40 41 68 72 69  .....Jovial@Ahri
0040: 6D 61 6E 00 00 B5 00 00  00 00                    man.......      
```

#### Opcodes

```
  0: 0x002D [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=264*)
  1: 0x0031 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x13 - Copy string and replace @ with space, work_offset=ExtData[1]->WorkLocal[0], string="Jovial@Ahriman")
  2: 0x0045 [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  3: 0x0049 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 29 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                B6 00 05 80 B4 00            ......
0050: 00 00 56 6F 72 74 69 6D  65 72 65 00 00 00 00 00  ..Vortimere.....
0060: 00 00 B5 00 00 00 00                              .......         
```

#### Opcodes

```
  0: 0x004A [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2705*)
  1: 0x004E [0xB4] UI_WINDOW_STRING_HANDLER(case=0x00 - Copy string from opcode, work_offset=ExtData[1]->WorkLocal[0], string="Vortimere")
  2: 0x0062 [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  3: 0x0066 [0x00] END_REQSTACK()
```
