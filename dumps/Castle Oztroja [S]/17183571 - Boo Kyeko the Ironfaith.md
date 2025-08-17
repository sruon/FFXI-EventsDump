# 17183571 - Boo Kyeko the Ironfaith

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Castle Oztroja [S] (ID: 99) |
| Block Size       | 108 bytes                   |
| Total Events     | 5                           |
| References Count | 7                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [100](#event-100)        | 0x0001       |      7 |              2 |
| [101](#event-101)        | 0x0008       |      7 |              2 |
| [65535.1](#event-655351) | 0x000F       |     15 |              5 |
| [65535.2](#event-655352) | 0x001E       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFDD7BF  |  4294825919 |
|       2 | 0x1883D     |      100413 |
|       3 | 0x00F9      |         249 |
|       4 | 0xFFFDC557  |  4294821207 |
|       5 | 0x18559     |       99673 |
|       6 | 0x00F6      |         246 |

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

### Event 100

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

### Event 101

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0008 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               32                 2
0010: 00 80 1F 00 01 80 02 80  03 80 1F 01 6F 00        ............o.  
```

#### Opcodes

```
  0: 0x000F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0012 [0x1F] MOVE_ENTITY: EventEntity moves to X=-141.377*, Z=100.413*, Y=0.249*
  2: 0x001A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001E   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            32 00                2.
0020: 80 1F 00 04 80 05 80 06  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x001E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0021 [0x1F] MOVE_ENTITY: EventEntity moves to X=-146.089*, Z=99.673*, Y=0.246*
  2: 0x0029 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002B [0x00] END_REQSTACK()
```
