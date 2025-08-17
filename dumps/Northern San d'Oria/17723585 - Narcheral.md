# 17723585 - Narcheral

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 184 bytes                     |
| Total Events     | 6                             |
| References Count | 8                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [688](#event-688)     | 0x0001       |      6 |              4 |
| [689](#event-689)     | 0x0007       |      1 |              1 |
| [690](#event-690)     | 0x0008       |     55 |             13 |
| [691](#event-691)     | 0x003F       |     46 |             10 |
| [692](#event-692)     | 0x006D       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x30C7      |       12487 |
|       1 | 0x0448      |        1096 |
|       2 | 0x30D0      |       12496 |
|       3 | 0x0014      |          20 |
|       4 | 0x30D1      |       12497 |
|       5 | 0x00C9      |         201 |
|       6 | 0x0000      |           0 |
|       7 | 0x30D2      |       12498 |

## String References

- **12487**: Behold the beauty of this cathedral. We failed to protect it once, but never again.
- **12496**: Yes, this is indeed $7. Our worst nightmare has come true.
- **12497**: This is for you. I foresee I will need your help yet again...
- **12498**: Excellent work, my friend. This is what I promised. We can only await Prince Pieuje's decision now.

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

### Event 688

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 6 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1D 00 80 23 21 00                               ...#!.         
```

#### Opcodes

```
  0: 0x0001 [0x1D] PRINT_EVENT_MESSAGE(message_id=12487*)
    → "Behold the beauty of this cathedral. We failed to protect it once, but never again."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x21] END_EVENT
  3: 0x0006 [0x00] END_REQSTACK()
```

### Event 689

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

### Event 690

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0008   |
| Data Size    | 55 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          42 1E F0 FF FF 7F 03 09          B.......
0010: 10 01 80 1D 02 80 23 6F  70 66 03 80 F8 FF FF 7F  ......#opf......
0020: F8 FF FF 7F 70 61 73 30  1D 04 80 23 45 05 80 F0  ....pas0...#E...
0030: FF FF 7F F0 FF FF 7F 71  73 74 63 06 80 21 00     .......qstc..!. 
```

#### Opcodes

```
  0: 0x0008 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0009 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x000E [0x03] Work_Zone[9] = 1096*
  3: 0x0013 [0x1D] PRINT_EVENT_MESSAGE(message_id=12496*)
    → "Yes, this is indeed $7. Our worst nightmare has come true."
  4: 0x0016 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0017 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0018 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x0019 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=20*
  8: 0x0028 [0x1D] PRINT_EVENT_MESSAGE(message_id=12497*)
    → "This is for you. I foresee I will need your help yet again..."
  9: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x002C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 11: 0x003D [0x21] END_EVENT
 12: 0x003E [0x00] END_REQSTACK()
```

### Event 691

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003F   |
| Data Size    | 46 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               42                 B
0040: 1E F0 FF FF 7F 6F 70 66  03 80 F8 FF FF 7F F8 FF  .....opf........
0050: FF 7F 70 61 73 30 1D 07  80 23 45 05 80 F0 FF FF  ..pas0...#E.....
0060: 7F F0 FF FF 7F 71 73 74  63 06 80 21 00           .....qstc..!.   
```

#### Opcodes

```
  0: 0x003F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0040 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0045 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0046 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0047 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=20*
  5: 0x0056 [0x1D] PRINT_EVENT_MESSAGE(message_id=12498*)
    → "Excellent work, my friend. This is what I promised. We can only await Prince Pieuje's decision now."
  6: 0x0059 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x005A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  8: 0x006B [0x21] END_EVENT
  9: 0x006C [0x00] END_REQSTACK()
```

### Event 692

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         00                     .  
```

#### Opcodes

```
  0: 0x006D [0x00] END_REQSTACK()
```
