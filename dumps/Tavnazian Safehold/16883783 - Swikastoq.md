# 16883783 - Swikastoq

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 148 bytes                   |
| Total Events     | 5                           |
| References Count | 12                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      7 |              2 |
| [234](#event-234)        | 0x0007       |      1 |              1 |
| [65535.1](#event-655351) | 0x0008       |     25 |              7 |
| [65535.2](#event-655352) | 0x0021       |     15 |              5 |
| [65535.3](#event-655353) | 0x0030       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFE72AB  |  4294865579 |
|       2 | 0xE957      |       59735 |
|       3 | 0xFFFF9495  |  4294939797 |
|       4 | 0xFFFE74FD  |  4294866173 |
|       5 | 0xE16E      |       57710 |
|       6 | 0xFFFF9688  |  4294940296 |
|       7 | 0xFFFE764E  |  4294866510 |
|       8 | 0xDA9E      |       55966 |
|       9 | 0xFFFE86DE  |  4294870750 |
|      10 | 0xA93A      |       43322 |
|      11 | 0xFFFF9689  |  4294940297 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0000 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x00] END_REQSTACK()
```

### Event 234

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0007  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      00                                  .        
```

#### Opcodes

```
  0: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0008   |
| Data Size    | 25 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          32 00 80 1F 00 01 80 02          2.......
0010: 80 03 80 1F 01 1F 00 04  80 05 80 06 80 1F 01 6F  ...............o
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0008 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000B [0x1F] MOVE_ENTITY: EventEntity moves to X=-101.717*, Z=59.735*, Y=-27.499*
  2: 0x0013 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0015 [0x1F] MOVE_ENTITY: EventEntity moves to X=-101.123*, Z=57.710*, Y=-27.000*
  4: 0x001D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x001F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0020 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    32 00 80 1F 00 07 80  08 80 06 80 1F 01 6F 00   2............o.
```

#### Opcodes

```
  0: 0x0021 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0024 [0x1F] MOVE_ENTITY: EventEntity moves to X=-100.786*, Z=55.966*, Y=-27.000*
  2: 0x002C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 32 00 80 1F 00 09 80 0A  80 0B 80 1F 01 6F 00     2............o. 
```

#### Opcodes

```
  0: 0x0030 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0033 [0x1F] MOVE_ENTITY: EventEntity moves to X=-96.546*, Z=43.322*, Y=-26.999*
  2: 0x003B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x003E [0x00] END_REQSTACK()
```
