# 17760441 - Dehn Harzhapan

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Port Windurst (ID: 240) |
| Block Size       | 268 bytes               |
| Total Events     | 6                       |
| References Count | 15                      |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [10014](#event-10014) | 0x0001       |     49 |             11 |
| [10015](#event-10015) | 0x0032       |     50 |             17 |
| [10016](#event-10016) | 0x0064       |     46 |              8 |
| [10017](#event-10017) | 0x0092       |     11 |              5 |
| [10018](#event-10018) | 0x009D       |     11 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x31F4      |       12788 |
|       1 | 0x0032      |          50 |
|       2 | 0x31F5      |       12789 |
|       3 | 0x31F6      |       12790 |
|       4 | 0x31F7      |       12791 |
|       5 | 0x31F8      |       12792 |
|       6 | 0x0001      |           1 |
|       7 | 0x0000      |           0 |
|       8 | 0x31F9      |       12793 |
|       9 | 0x40000000  |  1073741824 |
|      10 | 0x000A      |          10 |
|      11 | 0x31FA      |       12794 |
|      12 | 0x00C9      |         201 |
|      13 | 0x31FB      |       12795 |
|      14 | 0x31F3      |       12787 |

## String References

- **12787**: Ahhh, if only a strrrong, reliable adventurer would come by...
- **12788**: Well if it isn't a strrrong, reliable-looking adventurer! How'd you like to get your paws on a hefty reward?
- **12789**: There's this rich little Tarutaru that needs some help navigating thrrrough the Garlaige Citadel. You look like you'd be perrrfect for the job.
- **12790**: Your client's name is Wanzo-Unzozo. He should be waiting just inside the citadel's entrrrance.
- **12791**: Whoa, hold on. You're not thinking of slitherrring your way out of this job, are you?
- **12792**: Slithering your way out? [Like a snake./Not at all.]
- **12793**: I knew it! I don't know why I ever trusted you in the firrrst place...
- **12794**: Grrreat job, <Player>. I knew I could count on you to get the job done. Here's your reward.
- **12795**: Sorrrry, <Player>. I don't have any work for you today.

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

### Event 10014

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 49 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 66 01 80 F8 FF FF   ........#f.....
0010: 7F F8 FF FF 7F 74 6C 6B  30 1D 02 80 23 66 01 80  .....tlk0...#f..
0020: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 31 1D 03 80 23  ........tlk1...#
0030: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=12788*)
    → "Well if it isn't a strrrong, reliable-looking adventurer! How'd you like to get your paws on a hefty reward?"
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  4: 0x0019 [0x1D] PRINT_EVENT_MESSAGE(message_id=12789*)
    → "There's this rich little Tarutaru that needs some help navigating thrrrough the Garlaige Citadel. You look like you'd be perrrfect for the job."
  5: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=50*
  7: 0x002C [0x1D] PRINT_EVENT_MESSAGE(message_id=12790*)
    → "Your client's name is Wanzo-Unzozo. He should be waiting just inside the citadel's entrrrance."
  8: 0x002F [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0030 [0x21] END_EVENT
 10: 0x0031 [0x00] END_REQSTACK()
```

### Event 10015

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0032   |
| Data Size    | 50 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       1E F0 FF FF 7F 1D  03 80 23 1D 04 80 23 24    ........#...#$
0040: 05 80 06 80 07 80 25 02  00 10 07 80 00 5D 00 1D  ......%......]..
0050: 08 80 23 03 01 10 07 80  21 00 01 5D 00 03 01 10  ..#.....!..]....
0060: 09 80 21 00                                       ..!.            
```

#### Opcodes

```
  0: 0x0032 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0037 [0x1D] PRINT_EVENT_MESSAGE(message_id=12790*)
    → "Your client's name is Wanzo-Unzozo. He should be waiting just inside the citadel's entrrrance."
  2: 0x003A [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x003B [0x1D] PRINT_EVENT_MESSAGE(message_id=12791*)
    → "Whoa, hold on. You're not thinking of slitherrring your way out of this job, are you?"
  4: 0x003E [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x003F [0x24] CREATE_DIALOG(message_id=12792*, default_option=1*, option_flags=0*)
    → "Slithering your way out? [Like a snake./Not at all.]"
  6: 0x0046 [0x25] WAIT_DIALOG_SELECT()
  7: 0x0047 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x005D
  8: 0x004F [0x1D] PRINT_EVENT_MESSAGE(message_id=12793*)
    → "I knew it! I don't know why I ever trusted you in the firrrst place..."
  9: 0x0052 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0053 [0x03] Work_Zone[1] = 0*
 11: 0x0058 [0x21] END_EVENT
 12: 0x0059 [0x00] END_REQSTACK()

SUBROUTINE_005D:
 13: 0x005D [0x03] Work_Zone[1] = 1073741824*
 14: 0x0062 [0x21] END_EVENT
 15: 0x0063 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x005A [0x01] GOTO 0x005D
```

### Event 10016

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0064   |
| Data Size    | 46 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             1E F0 FF FF  7F 1C 0A 80 66 01 80 F8      ........f...
0070: FF FF 7F F8 FF FF 7F 70  61 73 30 1D 0B 80 23 45  .......pas0...#E
0080: 0C 80 F0 FF FF 7F F0 FF  FF 7F 71 73 74 63 07 80  ..........qstc..
0090: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0064 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0069 [0x1C] WAIT(10* ticks)
  2: 0x006C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=50*
  3: 0x007B [0x1D] PRINT_EVENT_MESSAGE(message_id=12794*)
    → "Grrreat job, <Player>. I knew I could count on you to get the job done. Here's your reward."
  4: 0x007E [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x007F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  6: 0x0090 [0x21] END_EVENT
  7: 0x0091 [0x00] END_REQSTACK()
```

### Event 10017

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0092   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:       1E F0 FF FF 7F 1D  0D 80 23 21 00             ........#!.   
```

#### Opcodes

```
  0: 0x0092 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0097 [0x1D] PRINT_EVENT_MESSAGE(message_id=12795*)
    → "Sorrrry, <Player>. I don't have any work for you today."
  2: 0x009A [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x009B [0x21] END_EVENT
  4: 0x009C [0x00] END_REQSTACK()
```

### Event 10018

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009D   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                         1E F0 FF               ...
00A0: FF 7F 1D 0E 80 23 21 00                           .....#!.        
```

#### Opcodes

```
  0: 0x009D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00A2 [0x1D] PRINT_EVENT_MESSAGE(message_id=12787*)
    → "Ahhh, if only a strrrong, reliable adventurer would come by..."
  2: 0x00A5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00A6 [0x21] END_EVENT
  4: 0x00A7 [0x00] END_REQSTACK()
```
